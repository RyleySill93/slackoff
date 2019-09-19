from rest_framework.decorators import api_view
from PIL import Image, ImageChops, ImageEnhance
import uuid
from emojis.settings import BASE_DIR
from django.http import HttpResponse
import base64
import boto3
import os
from rest_framework.response import Response
from rest_framework import status
from gifs.image_data import TrackedElement
from gifs import gifs_data
from .models import Image as ImageModel

S3_BUCKET = os.environ.get('S3_BUCKET')



type_map = dict(
    disappears=gifs_data.disappears,
)

@api_view(['GET'])
def get_urls(request):
    s3_client = boto3.client('s3')

    urls = []

    for image in ImageModel.objects.all():
        params = {'Bucket': S3_BUCKET, 'Key': image.s3_key}
        url = s3_client.generate_presigned_url('get_object', params)
        urls.append(dict(
            url=url,
            type=image.type,
            width=image.width,
            height=image.height,
        ))

    return Response(urls, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_gifs(request):
    s3_client = boto3.client('s3')

    urls = []

    params = {'Bucket': S3_BUCKET, 'Key': 'types/{}.gif'.format(request.GET['type'])}
    url = s3_client.generate_presigned_url('get_object', params)

    return Response({'url': url}, status=status.HTTP_200_OK)


def upload_file(file_path, file_name):
    s3_client = boto3.client('s3')
    s3_client.upload_file(file_path, S3_BUCKET, file_name)
    url = s3_client.generate_presigned_url('get_object',
                                    Params={
                                        'Bucket': S3_BUCKET,
                                        'Key': file_name,
                                    },
                                    ExpiresIn=3600)

    return url

def get_file_name_path():
    filename = str(uuid.uuid1())
    file_path = '{}/pics/{}'.format(BASE_DIR, '{}.gif'.format(filename))

    return filename, file_path

def get_duration(img):
    img = Image.open(img)
    frames = duration = 0
    while True:
        try:
            img.seek(frames)
            frames += 1
            duration += img.info['duration']
        except EOFError:
            return duration / frames
    return None


def get_generated_gif_url(payload, gif_type, reverse=False):
    frames = generate_gif_frames(gif_type, [TrackedElement(
        id=1,
        image_file=payload,
    )])

    if reverse:
        frames.reverse()

    key, file_path = get_file_name_path()

    duration = get_duration(gif_type.background_image_path)

    width, height = frames[0].size

    save_gif(file_path, frames, duration=duration)

    url = upload_file(file_path, key)

    ImageModel.objects.create(
        s3_key=key,
        type=gif_type.type,
        width=width,
        height=height,
    )

    os.remove(file_path)

    return url

def save_gif(file_path, frames, duration):
    frames[0].save(
        file_path,
        save_all=True,
        disposal=2,
        append_images=frames[1:],
        duration=duration,
        loop=0,
        optimize=True,
        quality=95,
        transparency=255
    )


def prep_file(file):
    im = Image.open(file)
    im = im.convert('RGBA')

    # make into a square
    width, height = im.size
    size = max(width, height)
    new_im = Image.new('RGBA', (size, size), 255)
    new_im.paste(im, (int((size - width) / 2), int((size - height) / 2)))

    # keep background transparent
    alpha = new_im.split()[3]
    im = new_im.convert('RGB').convert('P', palette=Image.ADAPTIVE, colors=255)
    mask = Image.eval(alpha, lambda a: 255 if a <= 128 else 0)
    im.paste(255, mask)

    im = im.resize((256, 256), Image.ANTIALIAS)

    return im


def resize(im, new_height):
    width, height = im.size
    resize_factor = height / new_height
    new_width = int(width / resize_factor)

    return im.resize((new_width, new_height), Image.ANTIALIAS)


def paste(tracked_element_position, frame, paste_image, x_adj, y_adj):
    width, height = paste_image.size
    half_width = int(width / 2)
    half_height = int(height / 2)

    x = tracked_element_position.x - half_width
    y = tracked_element_position.y - half_height

    frame.paste(paste_image, (x + x_adj, y + y_adj), mask=paste_image)


def generate_gif_frames(image_data, input_tracked_elements):
    background_image = Image.open(image_data.background_image_path)
    foreground_image = None

    if image_data.foreground_image_path:
        foreground_image = Image.open(image_data.foreground_image_path)

    frames = []

    for frame_index in range(0, background_image.n_frames):
        background_image.seek(frame_index)
        if image_data.foreground_image_path:
            frame = background_image.convert('RGB')
        else:
            frame = background_image.convert('RGBA')

        for tracked_element in input_tracked_elements:
            tracked_element_position = image_data.get_tracked_element_position(
                tracked_element_id=tracked_element.id,
                frame_index=frame_index,
            )

            if not tracked_element_position:
                continue

            adjustment = image_data.get_tracked_element_adjustment(
                tracked_element_id=tracked_element.id,
            )

            # resize
            paste_image = resize(tracked_element.image_file, tracked_element_position.height + (adjustment.height or 0))

            # rotate
            if tracked_element_position.rotation or adjustment.rotation:
                paste_image = paste_image.rotate((tracked_element_position.rotation or 0) + (adjustment.rotation or 0), expand=True)

            # brightness
            if tracked_element_position.brightness or adjustment.brightness:
                enhancer = ImageEnhance.Brightness(paste_image)
                paste_image = enhancer.enhance((tracked_element_position.brightness or 0) + (adjustment.brightness or 0))

            # paste
            paste(tracked_element_position, frame, paste_image, (adjustment.x or 0), (adjustment.y or 0))

        if image_data.foreground_image_path:
            if frame_index in image_data.foreground_indicies:
                foreground_image.seek(frame_index)
                msk = foreground_image.convert('RGBA')
                frame.paste(msk, mask=msk)
        else:
            # make added elements transparent - carlton turns green without this
            alpha = frame.split()[3]
            frame = frame.convert('RGB').convert('P', palette=Image.ADAPTIVE, colors=255)
            mask = Image.eval(alpha, lambda a: 255 if a <= 128 else 0)
            frame.paste(255, mask)

        # optimize frame
        # x, y = frame.size
        # x2, y2 = int(x / 2), int(y / 2)
        # frame = frame.resize((x2, y2), Image.ANTIALIAS)

        frames.append(frame)

    return frames


@api_view(['POST'])
def bobblify(request):
    start = -15
    end = 15
    degs = 5
    current = start

    frames = []

    im = prep_file(request.FILES['file'])

    while current <= end:
        frame = im.rotate(current, fillcolor=255)
        frames.append(frame)
        current += degs

    while current > start:
        frame = im.rotate(current, fillcolor=255)
        frames.append(frame)
        current -= degs

    file_name, file_path = get_file_name_path()

    frames[0].save(
        file_path,
        save_all=True,
        disposal=2,
        append_images=frames[1:],
        duration=40,
        transparency=255,
        loop=0,
        optimize=True,
        quality=95,
    )

    url = upload_file(file_path, file_name)

    os.remove(file_path)

    return Response({'url': url}, status=status.HTTP_200_OK)


@api_view(['POST'])
def intensify(request):
    frames = []

    im = prep_file(request.FILES['file'])

    width, height = im.size

    offset = int(width / 50)

    coords = [
        (offset, offset),
        (-offset, offset),
        (offset, -offset),
        (-offset, -offset),
        (offset, offset),
        (offset, -offset),
        (-offset, offset),
    ]

    for x, y in coords:
        a = 1
        b = 0
        c = x  # left/right (i.e. 5/-5)
        d = 0
        e = 1
        f = y  # up/down (i.e. 5/-5)
        frame = im.transform(im.size, Image.AFFINE, (a, b, c, d, e, f), fillcolor=255)

        frames.append(frame)

    file_name, file_path = get_file_name_path()

    frames[0].save(file_path,
                   save_all=True,
                   disposal=2,
                   append_images=frames[1:],
                   duration=40,
                   transparency=255,
                   loop=0,
                   optimize=True,
                   quality=95,
                   )

    url = upload_file(file_path, file_name)

    os.remove(file_path)

    return Response({'url': url}, status=status.HTTP_200_OK)


@api_view(['POST'])
def detective(request):
    new_im = Image.new('RGBA', (160, 160), 255)

    coat = Image.open('pics/coat.png')
    _, coat_height = coat.size
    y = 160 - coat_height

    new_im.paste(coat, (25, y))

    head = Image.open(request.FILES['file'])

    head_width, head_height = head.size
    new_head_width = 90

    resize_factor = (head_width / new_head_width)
    head = head.resize((new_head_width, int(head_height / resize_factor)), Image.ANTIALIAS)

    head_width, head_height = head.size

    center_x = 82
    half_head_width = int(head_width / 2)
    x = center_x - half_head_width
    new_im.paste(head, (x, 15), mask=head)

    hat = Image.open('pics/hat.png')
    hat_width, _ = hat.size
    x = int((160 - hat_width) / 2)

    new_im.paste(hat, (16, 0), mask=hat)

    file_name = '{}.png'.format(uuid.uuid1())
    file_path = '{}/pics/{}'.format(BASE_DIR, file_name)

    new_im.save(file_path)

    url = upload_file(file_path, file_name)

    os.remove(file_path)

    return Response({'url': url}, status=status.HTTP_200_OK)


@api_view(['POST'])
def approves(request):
    im = prep_file(request.FILES['file'])


def bush_frames(file, emerge=False):
    points = [
        (242, 100),  # 1
        (242, 100),  # 2
        (242, 100),  # 3
        (242, 100),  # 4
        (242, 100),  # 5
        (242, 100),  # 6
        (242, 100),  # 7
        (242, 100),  # 8
        (244, 100),  # 9
        (240, 100),  # 10
        (241, 100),  # 11
        (248, 104),  # 12
        (248, 104),  # 13
        (250, 105),  # 14
        (248, 107),  # 15
        (249, 106),  # 16
        (252, 108),  # 17
        (255, 111),  # 18
        (257, 112),  # 19
        (259, 113),  # 20
        (262, 115),  # 21
        (262, 115),  # 22
        (266, 119),  # 23
        (269, 118),  # 24
        (273, 121),  # 25
        (276, 122),  # 26
        (278, 122),  # 27
        (279, 122),  # 28
        (275, 123),  # 29
        (276, 121),  # 30
        (277, 121),  # 31
        (280, 123),  # 32
        (277, 123),  # 33
        (277, 123),  # 34
        (272, 123),  # 35
        (272, 122),  # 36
        (266, 124),  # 37
        (265, 123),  # 38
        (265, 123),  # 39
        (267, 123),  # 40
        (268, 124),  # 41
        (268, 123),  # 42
        (270, 123),  # 43
        (272, 122),  # 44
        (272, 122),  # 45
        (276, 123),  # 46
        (276, 123),  # 47
        (276, 123),  # 48
        (276, 123),  # 49
        (276, 123),  # 50
    ]

    im = Image.open(file)

    width, height = im.size
    head_width = 130
    resize_factor = width / head_width
    head_height = int(height / resize_factor)
    im = im.resize((head_width, head_height), Image.ANTIALIAS)

    half_width = int(head_width / 2)
    half_height = int(head_height / 2)

    base_homer = Image.open("pics/homer.gif")
    mask_homer = Image.open("pics/homermask.gif")
    frames = []

    for i in range(0, base_homer.n_frames):
        base_homer.seek(i)
        frame = base_homer.convert('RGB')
        if i < len(points):
            x = points[i][0] - half_width
            y = points[i][1] - half_height
            frame.paste(im, (x + 10, y), mask=im)

            if i >= 23:
                mask_homer.seek(i - 23)
                mask = mask_homer.convert('RGBA')
                frame.paste(mask, mask=mask)

        frames.append(frame)

    if emerge:
        frames.reverse()

    return frames


@api_view(['POST'])
def disappears(request):
    im = Image.open(request.FILES['file'])

    url = get_generated_gif_url(payload=im, gif_type=gifs_data.disappears)

    return Response({'url': url}, status=status.HTTP_200_OK)


@api_view(['POST'])
def magic(request):
    im = Image.open(request.FILES['file'])

    url = get_generated_gif_url(payload=im, gif_type=gifs_data.magic)

    return Response({'url': url}, status=status.HTTP_200_OK)


@api_view(['POST'])
def begging(request):
    im = Image.open(request.FILES['file'])

    url = get_generated_gif_url(payload=im, gif_type=gifs_data.begging)

    return Response({'url': url}, status=status.HTTP_200_OK)


@api_view(['POST'])
def appears(request):
    im = Image.open(request.FILES['file'])

    url = get_generated_gif_url(payload=im, gif_type=gifs_data.disappears, reverse=True)

    return Response({'url': url}, status=status.HTTP_200_OK)


@api_view(['POST'])
def time(request):
    im = Image.open(request.FILES['file'])

    url = get_generated_gif_url(payload=im, gif_type=gifs_data.time)

    return Response({'url': url}, status=status.HTTP_200_OK)


@api_view(['POST'])
def carlton(request):
    im = Image.open(request.FILES['file'])

    url = get_generated_gif_url(payload=im, gif_type=gifs_data.carlton)

    return Response({'url': url}, status=status.HTTP_200_OK)


@api_view(['POST'])
def supa_hot_fire(request):

    im = Image.open(request.FILES['file'])

    url = get_generated_gif_url(payload=im, gif_type=gifs_data.supa_hot_fire)

    return Response({'url': url}, status=status.HTTP_200_OK)


@api_view(['POST'])
def strut(request):
    im = Image.open(request.FILES['file'])

    url = get_generated_gif_url(payload=im, gif_type=gifs_data.strut)

    return Response({'url': url}, status=status.HTTP_200_OK)


@api_view(['POST'])
def hide(request):
    im = Image.open(request.FILES['file'])

    url = get_generated_gif_url(payload=im, gif_type=gifs_data.hide)

    return Response({'url': url}, status=status.HTTP_200_OK)


@api_view(['POST'])
def chimp(request):
    im = Image.open(request.FILES['file'])

    url = get_generated_gif_url(payload=im, gif_type=gifs_data.chimp)

    return Response({'url': url}, status=status.HTTP_200_OK)


@api_view(['POST'])
def computer_kid(request):
    im = Image.open(request.FILES['file'])

    url = get_generated_gif_url(payload=im, gif_type=gifs_data.computer_kid)

    return Response({'url': url}, status=status.HTTP_200_OK)


@api_view(['POST'])
def toast(request):
    im = Image.open(request.FILES['file'])

    url = get_generated_gif_url(payload=im, gif_type=gifs_data.toast)

    return Response({'url': url}, status=status.HTTP_200_OK)


@api_view(['POST'])
def fire(request):
    im = Image.open(request.FILES['file'])

    url = get_generated_gif_url(payload=im, gif_type=gifs_data.fire)

    return Response({'url': url}, status=status.HTTP_200_OK)


@api_view(['POST'])
def trump(request):
    im = Image.open(request.FILES['file'])

    url = get_generated_gif_url(payload=im, gif_type=gifs_data.trump)

    return Response({'url': url}, status=status.HTTP_200_OK)


@api_view(['POST'])
def clapping(request):
    im = Image.open(request.FILES['file'])
    converter = ImageEnhance.Color(im)
    im = converter.enhance(0)

    url = get_generated_gif_url(payload=im, gif_type=gifs_data.clapping)

    return Response({'url': url}, status=status.HTTP_200_OK)


@api_view(['POST'])
def thinking(request):
    im = Image.open(request.FILES['file'])

    url = get_generated_gif_url(payload=im, gif_type=gifs_data.thinking)

    return Response({'url': url}, status=status.HTTP_200_OK)


@api_view(['POST'])
def mind_blown(request):
    im = Image.open(request.FILES['file'])

    url = get_generated_gif_url(payload=im, gif_type=gifs_data.mind_blown)

    return Response({'url': url}, status=status.HTTP_200_OK)


@api_view(['POST'])
def left_hanging(request):
    im = Image.open(request.FILES['file'])

    url = get_generated_gif_url(payload=im, gif_type=gifs_data.left_hanging)

    return Response({'url': url}, status=status.HTTP_200_OK)


@api_view(['POST'])
def trapped(request):
    im = Image.open(request.FILES['file'])

    url = get_generated_gif_url(payload=im, gif_type=gifs_data.let_me_in)

    return Response({'url': url}, status=status.HTTP_200_OK)


@api_view(['POST'])
def javert(request):
    im = Image.open(request.FILES['file'])

    url = get_generated_gif_url(payload=im, gif_type=gifs_data.javert)

    return Response({'url': url}, status=status.HTTP_200_OK)


@api_view(['POST'])
def wrecking_ball(request):
    im = Image.open(request.FILES['file'])

    url = get_generated_gif_url(payload=im, gif_type=gifs_data.wrecking_ball)

    return Response({'url': url}, status=status.HTTP_200_OK)


@api_view(['POST'])
def heres_johnny(request):
    im = Image.open(request.FILES['file'])

    url = get_generated_gif_url(payload=im, gif_type=gifs_data.heres_johnny)

    return Response({'url': url}, status=status.HTTP_200_OK)
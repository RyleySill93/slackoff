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
from gifs.gifs_data import types

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
def get_gif_types(request):
    s3_client = boto3.client('s3')

    urls = []

    for image_type in types:
        params = {'Bucket': S3_BUCKET, 'Key': 'types/{}.gif'.format(image_type.image_data.type)}
        url = s3_client.generate_presigned_url('get_object', params)
        urls.append(dict(
            url=url,
            type=image_type.image_data.type,
            width=image_type.image_data.width,
            height=image_type.image_data.height,
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
    frames = generate_gif_frames(gif_type, [
        TrackedElement(
            id=i + 1,
            image_file=Image.open(payload['file/{}'.format(i)]),
        )
        for i, element in enumerate(payload)
    ])

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
def make_gif(request):
    if request.data['type'] == 'clapping':
        im = Image.open(request.FILES['file'])
        converter = ImageEnhance.Color(im)
        im = converter.enhance(0)

    url = get_generated_gif_url(payload=request.FILES, gif_type=getattr(gifs_data, request.data['type']))

    return Response({'url': url}, status=status.HTTP_200_OK)


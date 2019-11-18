from rest_framework.decorators import api_view
from PIL import Image, ImageChops, ImageEnhance
import uuid
from emojis.settings import BASE_DIR
import boto3
import os
from rest_framework.response import Response
from rest_framework import status
from gifs.image_data import TrackedElement as TE
from .models import Image as ImageModel, ImageData, TrackedElementPosition, FrameData, TrackedElement

S3_BUCKET = os.environ.get('S3_BUCKET')


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

    for image in ImageModel.objects.filter(is_base_gif=True):
        params = {'Bucket': S3_BUCKET, 'Key': 'types/{}.gif'.format(image.type)}
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

    params = {'Bucket': S3_BUCKET, 'Key': 'types/{}.gif'.format(request.GET['type'])}
    url = s3_client.generate_presigned_url('get_object', params)

    return Response(
        {
            'url': url,
            'tracked_element_ids': [te.id for te in TrackedElement.objects.filter(image_data__type=request.GET['type'])]
        },
        status=status.HTTP_200_OK
    )


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
    frames = generate_gif_frames_v2(gif_type, [
        TE(
            id=element,
            image_file=Image.open(payload[element]),
        ) for element in payload
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


def generate_gif_frames_v2(image_data, input_tracked_elements):
    background_image = Image.open(image_data.background_image_path)
    foreground_image = None

    if image_data.foreground_image_path:
        foreground_image = Image.open(image_data.foreground_image_path)

    frames = []

    for frame_index in range(0, background_image.n_frames):
        background_image.seek(frame_index)
        frame_data = FrameData.objects.get(
            index=frame_index,
            image_data=image_data,
        )
        if image_data.foreground_image_path:
            frame = background_image.convert('RGB')
        else:
            frame = background_image.convert('RGBA')

        for tracked_element in input_tracked_elements:
            tracked_element_position = TrackedElementPosition.objects.get(
                tracked_element_id=tracked_element.id,
                frame_data=frame_data,
            )

            if not tracked_element_position:
                continue

            adjustment = TrackedElementPosition.objects.get(
                tracked_element=tracked_element.id,
                frame_data__isnull=True,

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
            if frame_data.has_foreground:
                foreground_image.seek(frame_index)
                msk = foreground_image.convert('RGBA')
                frame.paste(msk, mask=msk)
        else:
            # make added elements transparent - carlton turns green without this
            alpha = frame.split()[3]
            frame = frame.convert('RGB').convert('P', palette=Image.ADAPTIVE, colors=255)
            mask = Image.eval(alpha, lambda a: 255 if a <= 128 else 0)
            frame.paste(255, mask)

        frames.append(frame)

    return frames


@api_view(['POST'])
def make_gif(request):
    if request.data['type'] == 'clapping':
        im = Image.open(request.FILES['file'])
        converter = ImageEnhance.Color(im)
        im = converter.enhance(0)

    image_data = ImageData.objects.get(
        type=request.data['type'],
    )

    url = get_generated_gif_url(payload=request.FILES, gif_type=image_data)

    return Response({'url': url}, status=status.HTTP_200_OK)

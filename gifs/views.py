from rest_framework.decorators import api_view
from PIL import Image, ImageChops
import uuid
from emojis.settings import BASE_DIR
from django.http import HttpResponse
import base64
import boto3
import os
from rest_framework.response import Response
from rest_framework import status


S3_BUCKET = os.environ.get('S3_BUCKET')


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

    file_name = '{}.gif'.format(uuid.uuid1())
    file_path = '{}/pics/{}'.format(BASE_DIR, file_name)

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

    file_name = '{}.gif'.format(uuid.uuid1())
    file_path = '{}/pics/{}'.format(BASE_DIR, file_name)

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

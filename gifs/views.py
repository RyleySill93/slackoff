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

    new_im.show()

    new_im.save(file_path,
                   # optimize=True,
                   # quality=95,
                   )

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
    frames = bush_frames(request.FILES['file'])
    file_name = '{}.gif'.format(uuid.uuid1())
    file_path = '{}/pics/{}'.format(BASE_DIR, file_name)

    frames[0].save(file_path,
                   save_all=True,
                   disposal=2,
                   append_images=frames[1:],
                   duration=60,
                   transparency=255,
                   loop=0,
                   optimize=True,
                   quality=95,
                   )

    url = upload_file(file_path, file_name)

    os.remove(file_path)

    return Response({'url': url}, status=status.HTTP_200_OK)


@api_view(['POST'])
def appears(request):
    frames = bush_frames(request.FILES['file'], emerge=True)
    file_name = '{}.gif'.format(uuid.uuid1())
    file_path = '{}/pics/{}'.format(BASE_DIR, file_name)

    frames[0].save(file_path,
                   save_all=True,
                   disposal=2,
                   append_images=frames[1:],
                   duration=60,
                   transparency=255,
                   loop=0,
                   optimize=True,
                   quality=95,
                   )

    url = upload_file(file_path, file_name)

    os.remove(file_path)

    return Response({'url': url}, status=status.HTTP_200_OK)


@api_view(['POST'])
def carlton_dance(request):
    points = [
        (97, 127),  # 1
        (98, 127),  # 2
        (96, 130),  # 3
        (98, 130),  # 4
        (108, 130),  # 5
        (112, 129),  # 6
        (123, 135),  # 7
        (122, 133),  # 8
        (113, 129),  # 9
        (106, 127),  # 10
        (98, 125),  # 11
        (97, 125),  # 12
        (100, 129),  # 13
        (101, 131),  # 14
        (102, 132),  # 15
        (99, 133),  # 16
        (90, 139),  # 17
        (84, 142),  # 18
        (74, 145),  # 19
        (73, 147),  # 20
        (80, 138),  # 21
        (88, 133),  # 22
        (97, 126),  # 23
        (96, 123),  # 24
    ]

    im = Image.open(request.FILES['file'])

    width, height = im.size
    head_width = 50
    resize_factor = width / head_width
    head_height = int(height / resize_factor)
    im = im.resize((head_width, head_height), Image.ANTIALIAS)

    half_width = int(head_width / 2)
    half_height = int(head_height / 2)


    carlton = Image.open("pics/carlton.gif")

    frames = []

    for i in range(0, carlton.n_frames):
        carlton.seek(i)
        frame = carlton.convert('RGBA')
        x = points[i][0] - half_width
        y = points[i][1] - half_height
        frame.paste(im, (x + 10, y), mask=im)

        # transparency
        alpha = frame.split()[3]
        frame = frame.convert('RGB').convert('P', palette=Image.ADAPTIVE, colors=255)
        mask = Image.eval(alpha, lambda a: 255 if a <= 128 else 0)
        frame.paste(255, mask)

        frames.append(frame)

    file_name = '{}.gif'.format(uuid.uuid1())
    file_path = '{}/pics/{}'.format(BASE_DIR, file_name)

    frames[0].save(file_path,
                   save_all=True,
                   disposal=2,
                   append_images=frames[1:],
                   duration=60,
                   loop=0,
                   optimize=True,
                   quality=95,
                   transparency=255
                   )

    url = upload_file(file_path, file_name)

    os.remove(file_path)

    return Response({'url': url}, status=status.HTTP_200_OK)


@api_view(['POST'])
def rap_battle(request):
    points = [
        (158, 88),  # 1
        (157, 88),  # 2
        (155, 88),  # 3
        (155, 88),  # 4
        (155, 88),  # 5
        (152, 87),  # 6
        (151, 87),  # 7
        (149, 85),  # 8
        (146, 84),  # 9
        (142, 84),  # 10
        (139, 83),  # 11
        (138, 83),  # 12
        (136, 82),  # 13
        (133, 84),  # 14
        (132, 84),  # 15
        (129, 83),  # 16
        (130, 82),  # 17
        (127, 80),  # 18
        (125, 79),  # 19
        (124, 77),  # 20
        (123, 75),  # 21
        (123, 75),  # 22
        (121, 72),  # 23
        (120, 69),  # 24
        (120, 66),  # 25
        (121, 63),  # 26
        (121, 63),  # 27
        (124, 60),  # 28
        (124, 60),  # 29
        (127, 58),  # 30
        (129, 58),  # 31
        (129, 58),  # 32
        (130, 61),  # 33
        (130, 61),  # 34
        (130, 62),  # 35
        (133, 65),  # 36
        (137, 67),  # 37
        (140, 70),  # 38
        (144, 73),  # 39
        (149, 76),  # 40
        (149, 76),  # 41
        (147, 73),  # 42
        (150, 76),  # 43
        (155, 79),  # 44
        (155, 79),  # 45
        (158, 80),  # 46
        (160, 83),  # 47
        (160, 85),  # 48
        (160, 85),  # 49
        (159, 86),  # 50
        (159, 86),  # 51
    ]

    im = Image.open(request.FILES['file'])

    width, height = im.size
    head_width = 70
    resize_factor = width / head_width
    head_height = int(height / resize_factor)
    im = im.resize((head_width, head_height), Image.ANTIALIAS)

    half_width = int(head_width / 2)
    half_height = int(head_height / 2)

    base_rap = Image.open("pics/rap.gif")
    rap_mask = Image.open("pics/rapmask.gif")
    frames = []

    for i in range(0, base_rap.n_frames):
        base_rap.seek(i)
        frame = base_rap.convert('RGB')
        if i < len(points):
            x = points[i][0] - half_width
            y = points[i][1] - half_height
            frame.paste(im, (x, y), mask=im)

            if i >= 24:
                rap_mask.seek(i)
                mask = rap_mask.convert('RGBA')
                frame.paste(mask, mask=mask)

        frames.append(frame)

    file_name = '{}.gif'.format(uuid.uuid1())
    file_path = '{}/pics/{}'.format(BASE_DIR, file_name)

    frames[0].save(file_path,
                   save_all=True,
                   disposal=2,
                   append_images=frames[1:],
                   duration=60,
                   transparency=255,
                   loop=0,
                   optimize=True,
                   quality=95,
    )

    url = upload_file(file_path, file_name)

    os.remove(file_path)

    return Response({'url': url}, status=status.HTTP_200_OK)


def resize(im, resize_height):
    width, height = im.size
    resize_factor = height / resize_height
    head_width = int(width / resize_factor)
    return im.resize((head_width, resize_height), Image.ANTIALIAS)


@api_view(['POST'])
def strut(request):
    points = [
        (125, 85, 18),  # 1
        (126, 82, 21),  # 2
        (129, 80, 23),  # 3
        (129, 78, 24),  # 4
        (130, 74, 25),  # 5
        (129, 68, 26),  # 6
        (127, 63, 27),  # 7
        (126, 60, 28),  # 8
        (125, 58, 29),  # 9
        (124, 58, 32),  # 10
        (118, 55, 34),  # 11
        (112, 55, 37),  # 12
        (111, 52, 40),  # 13
        (111, 47, 43),  # 14
        (116, 43, 43),  # 15
        (119, 43, 44),  # 16
        (122, 46, 44),  # 17
        (126, 51, 47),  # 18
        (135, 54, 51),  # 19
        (149, 52, 53),  # 20
        (155, 51, 56),  # 21
        (155, 45, 57),  # 22
        (152, 39, 57),  # 23
        (151, 35, 56),  # 24
        (151, 37, 54),  # 25
        (149, 43, 57),  # 26
        (142, 48, 57),  # 27
        (128, 47, 58),  # 28
        (116, 48, 60),  # 29
        (112, 45, 60),  # 30
        (116, 39, 58),  # 31
        (121, 37, 55),  # 32
        (122, 39, 55),  # 33
        (118, 44, 57),  # 34
    ]

    im = Image.open(request.FILES['file'])

    base = Image.open("pics/strut.gif")

    frames = []

    for i in range(0, base.n_frames):
        base.seek(i)
        frame = base.convert('RGBA')

        resized_im = resize(im, points[i][2] + 25)

        head_width, head_height = resized_im.size

        half_width = int(head_width / 2)
        half_height = int(head_height / 2)

        x = points[i][0] - half_width
        y = points[i][1] - half_height
        frame.paste(resized_im, (x, y), mask=resized_im)

        # transparency
        alpha = frame.split()[3]
        frame = frame.convert('RGB').convert('P', palette=Image.ADAPTIVE, colors=255)
        mask = Image.eval(alpha, lambda a: 255 if a <= 128 else 0)
        frame.paste(255, mask)

        frames.append(frame)

    file_name = '{}.gif'.format(uuid.uuid1())
    file_path = '{}/pics/{}'.format(BASE_DIR, file_name)

    frames[0].save(file_path,
                   save_all=True,
                   disposal=2,
                   append_images=frames[1:],
                   duration=60,
                   transparency=255,
                   loop=0,
                   optimize=True,
                   quality=95,
    )

    url = upload_file(file_path, file_name)

    os.remove(file_path)

    return Response({'url': url}, status=status.HTTP_200_OK)


@api_view(['POST'])
def trapped(request):
    points = [
        (268, 109, 186),  # 1
        (269, 111, 186),  # 2
        (271, 124, 186),  # 3
        (270, 136, 189),  # 4
        (266, 130, 190),  # 5
        (270, 129, 200),  # 6
        (266, 131, 209),  # 7
        (273, 132, 215),  # 8
        (283, 129, 223),  # 9
        (290, 121, 225),  # 10
        (298, 117, 230),  # 11
        (303, 111, 235),  # 12
        (304, 109, 240),  # 13
        (304, 103, 245),  # 14
        (303, 94, 250),  # 15
        (303, 96, 255),  # 16
        (292, 98, 260),  # 17
    ]

    im = Image.open(request.FILES['file'])


    base = Image.open("pics/conan.gif")
    mask = Image.open("pics/mask.gif")
    frames = []

    for i in range(0, base.n_frames):
        base.seek(i)
        resized_im = resize(im, points[i][2] + 30)
        head_width, head_height = resized_im.size

        half_width = int(head_width / 2)
        half_height = int(head_height / 2)

        frame = base.convert('RGB')
        x = points[i][0] - half_width
        y = points[i][1] - half_height
        frame.paste(resized_im, (x + 15, y - 10), mask=resized_im)

        mask.seek(i)
        msk = mask.convert('RGBA')
        frame.paste(msk, mask=msk)

        frames.append(frame)

    file_name = '{}.gif'.format(uuid.uuid1())
    file_path = '{}/pics/{}'.format(BASE_DIR, file_name)

    frames[0].save(file_path,
                   save_all=True,
                   disposal=2,
                   append_images=frames[1:],
                   duration=135,
                   transparency=255,
                   loop=0,
                   optimize=True,
                   quality=95,
                   )

    url = upload_file(file_path, file_name)

    os.remove(file_path)

    return Response({'url': url}, status=status.HTTP_200_OK)

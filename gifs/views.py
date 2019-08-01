from rest_framework.decorators import api_view
from PIL import Image, ImageChops
import uuid
from emojis.settings import BASE_DIR
from django.http import HttpResponse
import base64


@api_view(['POST'])
def bobblify(request):
    start = -30
    end = 0
    degs = 5
    current = start

    frames = []

    im = Image.open(request.FILES['file'])

    alpha = im.split()[3]
    im = im.convert('RGB').convert('P', palette=Image.ADAPTIVE, colors=255)
    mask = Image.eval(alpha, lambda a: 255 if a <= 128 else 0)
    im.paste(255, mask)

    while current <= end:
        frame = im.rotate(current, fillcolor=255)
        frames.append(frame)
        current += degs

    while current > start:
        frame = im.rotate(current, fillcolor=255)
        frames.append(frame)
        current -= degs

    file_name = '{}/pics/{}.gif'.format(BASE_DIR, uuid.uuid1())

    frames[0].save(
        file_name,
        save_all=True,
        disposal=2,
        append_images=frames[1:],
        duration=40,
        transparency=255,
        loop=0
    )

    image_data = open(file_name, "rb").read()

    meow = base64.b64encode(image_data)

    return HttpResponse(meow, content_type="image/png")


@api_view(['POST'])
def intensify(request):
    frames = []

    im = Image.open(request.FILES['file'])

    alpha = im.split()[3]
    im = im.convert('RGB').convert('P', palette=Image.ADAPTIVE, colors=255)
    mask = Image.eval(alpha, lambda a: 255 if a <= 128 else 0)
    im.paste(255, mask)

    coords = [
        (10, 10),
        (-10, 10),
        (10, -10),
        (-10, -10),
        (10, 10),
        (10, -10),
        (-10, 10),
    ]

    for x, y in coords:
        frame = ImageChops.offset(im, x, y)
        frames.append(frame)

    file_name = '{}/pics/{}.gif'.format(BASE_DIR, uuid.uuid1())
    frames[0].save(file_name,
                   save_all=True,
                   disposal=2,
                   append_images=frames[1:],
                   duration=40,
                   transparency=255,
                   loop=0)

    image_data = open(file_name, "rb").read()

    meow = base64.b64encode(image_data)

    return HttpResponse(meow, content_type="image/png")

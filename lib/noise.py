from PIL import Image

from opensimplex import OpenSimplex


FEATURE_SIZE = 24.0
simplex = OpenSimplex()


def noise2d(width=512, height=512):
    im = Image.new('L', (width, height))
    for y in range(0, height):
        for x in range(0, width):
            value = simplex.noise2d(x / FEATURE_SIZE, y / FEATURE_SIZE)
            color = int((value + 1) * 128)
            im.putpixel((x, y), color)
    im.save('noise2d.png')


def noise3d(width=512, height=512):
    im = Image.new('L', (width, height))
    for y in range(0, height):
        for x in range(0, width):
            value = simplex.noise3d(x / FEATURE_SIZE, y / FEATURE_SIZE, 0.0)
            color = int((value + 1) * 128)
            im.putpixel((x, y), color)
    im.save('noise3d.png')


def noise4d(width=512, height=512):
    im = Image.new('L', (width, height))
    for y in range(0, height):
        for x in range(0, width):
            value = simplex.noise4d(x / FEATURE_SIZE, y / FEATURE_SIZE, 0.0, 0.0)
            color = int((value + 1) * 128)
            im.putpixel((x, y), color)
    im.save('noise4d.png')
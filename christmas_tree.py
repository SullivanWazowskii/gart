import math

import svgwrite
from perlin_noise import PerlinNoise
from svgwrite.shapes import Polyline


def draw_spiral():
    points = []
    granularity = 100

    for i in range(0, granularity):
        c = 0
        r = i * 5
        noise = PerlinNoise()
        while c < 2 * math.pi:
            c = c + 0.01

            n = noise([r, c])
            x = r * math.cos(-n)
            y = r * math.sin(n)

            try:
                sig = 1 / (1 + math.exp(x / 1000))
            except OverflowError:
                sig = 1
            f = math.sin(math.pi * -11 * sig)

            x0 = x + 500
            y0 = y + 500
            xc = 500
            yc = 500
            rotate = 90 * math.pi / 180
            x1 = (x0 - xc) * math.cos(rotate) - (y0 - yc) * math.sin(rotate) + xc
            y1 = (x0 - xc) * math.sin(rotate) + (y0 - yc) * math.cos(rotate) + yc

            points.append((x1, y1))

    poly = Polyline(points=points, fill_opacity="0", stroke_width=1, stroke="green")
    dwg.add(poly)


def draw_to_file(file):
    global width, dwg
    width = 1000
    height = 1000

    dwg = svgwrite.Drawing(filename=file, size=(width, height), debug=True)
    dwg.add(dwg.rect(insert=(0, 0), size=(width, height), fill='white'))

    draw_spiral()

    dwg.save()


if __name__ == '__main__':
    draw_to_file(f"img/test{0}.svg")

import math
import random
from typing import Tuple

import cairosvg
from perlin_noise import PerlinNoise
from scipy.spatial.distance import euclidean
import svgwrite
from svgwrite.shapes import Polyline, Circle, Line

from magnets import FishEye, Harmonizer, Test


def draw_line(y_delta, pad, color):
    points = []
    granularity = 100
    for i in range(0, granularity):
        x = i * (width / granularity)
        # y = i * (height / granularity) + y_delta
        y = y_delta + pad
        # result_y1 = apply_magnet(x, y, magnet, force, -0.7)
        # result_y2 = apply_magnet(x, result_y1, magnet2, force * 0.9, 1)
        obj_apply = magnet_obj.apply((x, y))
        # obj_apply = hmagnet_obj.apply((obj_apply[0], obj_apply[1]))

        obj_apply = magnet4_obj.apply((obj_apply[0], obj_apply[1]))
        obj_apply = magnet3_obj.apply((obj_apply[0], obj_apply[1]))
        # obj_apply = magnet3_obj.apply((obj_apply[0], obj_apply[1]))

        # obj_apply = magnet_obj_fish.apply((obj_apply[0], obj_apply[1]))
        points.append((obj_apply[0], obj_apply[1]))
    poly = Polyline(points=points, fill_opacity="0", stroke_width=1, stroke=color)
    dwg.add(poly)


def draw_spiral():
    points = []
    granularity = 100
    noise = PerlinNoise(octaves=0.37)

    for i in range(0, 100):

        c = 0
        r = i * 4
        while c < 2 * math.pi:
            c = c + 0.2

            n = noise([c])

            x = r * math.cos(c)
            y = r * math.sin(c)

            #

            #
            # x0 = x + 500
            # y0 = y + 500
            # xc = 500
            # yc = 500
            # rotate = 90 * math.pi/180
            # x1 = (x0 - xc) * math.cos(rotate) - (y0 - yc) * math.sin(rotate) + xc
            # y1 = (x0 - xc) * math.sin(rotate) + (y0 - yc) * math.cos(rotate) + yc
            #
            points.append((x + 500 + n * 500, y + 500 ))

    poly = Polyline(points=points,
                    fill_opacity="0", stroke_width=1, stroke="green")
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
    cairosvg.svg2png(url=f"img/test{0}.svg", write_to=f"img/test{0}.png")

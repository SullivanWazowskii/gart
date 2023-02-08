import random
from typing import Tuple

import cairosvg
from perlin_noise import PerlinNoise
from scipy.spatial.distance import euclidean
import svgwrite
from svgwrite.shapes import Polyline, Circle, Line

from magnets import FishEye, Harmonizer, Test


def draw_octaves(y_delta, pad, color, noise):
    points = []
    granularity = 100

    for i in range(0, granularity):
        x = i * (width / granularity)
        # y = i * (height / granularity) + y_delta
        y = y_delta + pad

        n = noise([x/granularity, y/granularity])
        points.append((x, y+n*100))
    poly = Polyline(points=points, fill_opacity="0", stroke_width=1, stroke=color)
    dwg.add(poly)


def draw_to_file(file):
    global width, dwg, magnet_obj, magnet4_obj, magnet3_obj
    width = 1000
    height = 1000
    # for p in range(0, 5):
    dwg = svgwrite.Drawing(filename=file, size=(width, height), debug=True)
    dwg.add(dwg.rect(insert=(0, 0), size=(width, height), fill='white'))

    noise = PerlinNoise(octaves=0.77)
    for i in range(0, 200):
        draw_octaves(i*4, 100,
                     random.choice(["deeppink", "mediumvioletred"]), noise)

    dwg.save()


if __name__ == '__main__':
    draw_to_file(f"img/test{0}.svg")
    cairosvg.svg2png(url=f"img/test{0}.svg", write_to=f"img/test{0}.png")

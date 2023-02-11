from typing import Tuple

from scipy.spatial.distance import euclidean
import svgwrite
from svgwrite.shapes import Polyline, Circle, Line

from magnets import FishEye, Harmonizer


def draw_line(y_delta):
    points = []
    granularity = 10000
    for i in range(0, granularity):
        x = i * (width / granularity)
        # y = i * (height / granularity) + y_delta
        y = y_delta
        # result_y1 = apply_magnet(x, y, magnet, force, -0.7)
        # result_y2 = apply_magnet(x, result_y1, magnet2, force * 0.9, 1)
        obj_apply = magnet_obj.apply((x, y))
        obj_apply = magnet3_obj.apply((obj_apply[0], obj_apply[1]))
        # obj_apply = magnet3_obj.apply((obj_apply[0], obj_apply[1]))
        # obj_apply = magnet4_obj.apply((obj_apply[0], obj_apply[1]))
        # obj_apply = magnet_obj_fish.apply((obj_apply[0], obj_apply[1]))
        points.append((obj_apply[0], obj_apply[1] + 100))
    poly = Polyline(points=points, fill_opacity="0", stroke="black")
    dwg.add(poly)


# def draw_line2(y_delta):
#     points = []
#     granularity = 100
#     for i in range(0, granularity):
#         x = i * (width / granularity)
#         # y = height - i * (height / granularity) + y_delta
#         y = y_delta
#         # result_y1 = apply_magnet(x, y, magnet, force, -0.7)
#         # result_y2 = apply_magnet(x, result_y1, magnet2, force * 0.9, 1)
#         obj_apply = magnet_obj.apply((x, y))
#         # obj_apply = magnet3_obj.apply((obj_apply[0], obj_apply[1]))
#         # obj_apply = magnet4_obj.apply((obj_apply[0], obj_apply[1]))
#         points.append((obj_apply[0], min(max(0, obj_apply[1]), height)))
#     poly = Polyline(points=points, fill_opacity="0", stroke="black")
#     dwg.add(poly)


if __name__ == '__main__':
    width = 1000
    height = 1000

    # for p in range(0, 5):
    dwg = svgwrite.Drawing(filename=f"test{17}.svg", size=(width, height), debug=True)
    dwg.add(dwg.rect(insert=(0, 0), size=(width, height), fill='white'))

    magnet = [width / 3 - 47, height / 3 + 17]
    magnet2 = [2 * width / 3, - 2 * height / 3]
    magnet3 = [width / 2, - height / 2]
    magnet4 = [4 * width / 3, 4 * height / 3]

    magnet_obj = Harmonizer(magnet[0], magnet[1], 10, 50)

    magnet3_obj = Harmonizer(magnet3[0], magnet3[1], 10, 40)
    magnet4_obj = Harmonizer(magnet4[0], magnet4[1], 115, 50)
    # magnet_obj_fish = FishEye(width / 3 - 47, height / 3 + 17, 100, 0.5)
    # #
    dwg.add(Circle(center=tuple(magnet), r=magnet_obj.radius, fill='red'))
    # dwg.add(Circle(center=tuple(magnet2), r=10, fill='red'))
    dwg.add(Circle(center=tuple(magnet3), r=magnet3_obj.radius, fill='red'))
    # dwg.add(Circle(center=tuple(magnet4), r=10, fill='red'))
    # dwg.add(Line(start=(width / 2, 0), end=(width / 2, height), stroke="red"))
    # dwg.add(Line(start=(0, height / 2), end=(width, height / 2), stroke="red"))

    # force = 3.5
    #
    for i in range(0, 1000):
        draw_line(i * 3)
    # #
    # for i in range(1, 35):
    #     draw_line(i * -5)

    # for i in range(0, 50):
    #     draw_line2(i * 20)
    #
    # for i in range(0, 50):
    #     draw_line2(i * - 20)
    dwg.save()

from scipy.spatial.distance import euclidean
import svgwrite
from svgwrite.shapes import Polyline, Circle, Line


def apply_magnet(x, y, m, f, d):
    distance = euclidean([x, y], m)
    normed_distance = distance / ((width + height) / 4)
    # print(f"{euclidean} , {normed_distance}")
    # like tylor series
    # https://en.wikipedia.org/wiki/Taylor_series
    result_y = y + d * pow(normed_distance * 3, f)
    return result_y


def draw_line(y_delta):
    points = []
    granularity = 200
    for i in range(0, granularity):
        x = i * (width / granularity) + pow(i, 1.17) - y_delta
        y = i * (height / granularity) + y_delta
        result_y1 = apply_magnet(x, y, magnet, force, -1)
        result_y2 = apply_magnet(x, result_y1, magnet2, force, 1)
        points.append((x-150, min(max(0, result_y2 - 150), height)))
    poly = Polyline(points=points, fill_opacity="0", stroke="black")
    dwg.add(poly)


if __name__ == '__main__':
    width = 1000
    height = 1000

    dwg = svgwrite.Drawing(filename=f"test{17}.svg", size=(width, height), debug=True)
    dwg.add(dwg.rect(insert=(0, 0), size=(width, height), fill='white'))

    magnet = [1 * width / 2, 1 * height / 3]
    magnet2 = [1.6 * width / 2, 0.8 * height]
    magnet3 = [2.5 * width / 3, height / 3]
    magnet4 = [width / 3, 2 * height / 3]

    force = 4

    for i in range(0, 50):
        draw_line(i * 5)


    dwg.save()

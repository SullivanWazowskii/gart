import svgwrite
from svgwrite.shapes import Polyline


def print_hi(name):
    dwg = svgwrite.Drawing(filename="test.svg", size=(1000, 1000), debug=True)
    dwg.add(dwg.rect(insert=(0, 0), size=(1000, 1000), fill='white'))

    dwg.add(dwg.ellipse(center=(198.931, 249.512), r=(60, 36),
                        fill_opacity=".5", fill="orange", stroke="black", stroke_width="2"))
    dwg.add(dwg.ellipse(center=(265.779, 75.778), r=(36, 60), fill="orange", stroke="black", stroke_width="2"))

    dwg.add(
        dwg.path(d='M 0 320 L 40 280 A 30 60 0 0 1 150.71 170.29 L 172.55 152.45 A 30 50 -45 0 1 215.1 109.9 L 315 10',
                 stroke='black', stroke_width=2, fill='green', fill_opacity=".5"))
    poly = Polyline(points=[(0, 1000), (500, 500), (600, 100), (700, 1000)],
                    fill='green', fill_opacity="0.4", stroke="black")
    dwg.add(poly)


    dwg.save()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import math
from typing import Tuple
from perlin_noise import PerlinNoise

from scipy.spatial.distance import euclidean


class FishEye:

    def __init__(self, x, y, radius, force):
        self.x = x
        self.y = y
        self.radius = radius
        self.force = force

    def apply(self, point: Tuple) -> Tuple:
        point_x = point[0]
        point_y = point[1]
        distance = euclidean([point_x, point_y], [self.x, self.y])

        if distance > self.radius:
            return point

        normed_distance = distance / self.radius
        forced_distance = pow(normed_distance, self.force)
        t = forced_distance

        x = (1 - t) * self.x + t * point_x
        y = (1 - t) * self.y + t * point_y

        dx = x - point_x
        dy = y - point_y
        return point_x - dx, point_y - dy


class Harmonizer:

    def __init__(self, x, y, radius, force):
        self.x = x
        self.y = y
        self.radius = radius
        self.force = force

    def apply(self, point: Tuple) -> Tuple:
        point_x = point[0]
        point_y = point[1]

        # distance = euclidean([point_x, point_y], [self.x, self.y])

        # if distance > self.radius:
        #     return point

        # rate = distance / self.radius

        dy = self.x - point_x
        dx = self.y - point_y

        angle = math.atan2(dy, dx) * self.force
        sx = math.cos(angle)
        sy = math.sin(angle)

        return point_x + sx, point_y + sy


class Test:

    def __init__(self, x, y, radius, force, i):
        self.x = x
        self.y = y
        self.radius = radius
        self.force = force
        self.i = i
        self.noise = PerlinNoise()
        self.noise2 = PerlinNoise()

    def apply(self, point: Tuple) -> Tuple:
        point_x = point[0]
        point_y = point[1]

        distance = euclidean([point_x, point_y], [self.x, self.y])

        # rate = distance / self.radius
        #
        # dy = self.x - point_x
        # dx = self.y - point_y
        #
        # angle = math.atan2(dy, dx) * self.force
        # sx = math.cos(angle)
        # sy = math.sin(angle)

        n = self.noise(coordinates=[point_x / 1000, point_y / 1000])
        n2 = self.noise(coordinates=[point_x / 1000, point_y / 1000])
        # print(f"{point_x}, {n}")
        # self.i = self.i + 1
        # rate = self.radius / distance
        try:

            sig = 1 / (1 + math.exp(point_x / 1000))
        except OverflowError:
            sig = 1
        # sig = math.atan(point_x)

        # f = max(math.cos(math.pi * distance / self.radius),
        #         math.sin(math.pi * min(1, distance / self.radius)))
        # f = min(math.cos(math.pi * sig * self.force),
        #         math.sin(math.pi * sig * self.force))
        f = math.sin(math.pi * self.force * sig)
        # f = min(math.cos(math.pi * min(0.3, distance / self.radius)),
        #         math.sin(math.pi * min(0.3, distance / self.radius)) * 1 / (self.radius / distance))
        # f = min(0.5, 1 / min(1, distance / self.radius))
        # f = min(f, )
        # print(f"[{distance}, {self.radius}, {f}]", end=", ")
        # if distance < self.radius:
        #
        #     print(sig)
        #     return point_x, point_y + n * 200 + abs(sig) * math.sin(
        #         pow(n, 6) * 500 * math.pi) * 1000
        # + n2 * math.cos(n2) * 1000
        return point_x, point_y + n * math.sin(n) * 4000 * f

import math
from typing import Tuple

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
        #
        # if distance > self.radius:
        #     return point

        dy = self.x - point_x
        dx = self.y - point_y

        angle = math.atan2(dy, dx) * self.force
        sx = math.cos(angle)
        sy = math.sin(angle)

        return point_x, point_y + sy * 10

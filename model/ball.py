"""Ball logic"""

import math


class Ball:
    """Ball logic"""

    def __init__(self, radius):
        self.radius = radius
        self.position = [0.0, 0.0]
        self.speed = [0.0, 0.0]
        self.rotated = 0.0
        self.rotation_speed = 0.0

    def contains_point(self, coords):
        """Detect if ball contains point with coordinates given"""
        return ((self.position[0] - coords[0]) ** 2 +
                (self.position[1] - coords[1]) ** 2 <= self.radius ** 2)

    def get_weight(self):
        """Calculate weight"""
        return math.pi * self.radius ** 2

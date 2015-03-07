"""Ball logic"""


class Ball:
    """Ball logic"""

    def __init__(self, radius):
        self.radius = radius
        self.position = [0.0, 0.0]
        self.speed = [0.0, 0.0]
        self.moving = True

    def contains_point(self, coords):
        """Detect if ball contains point with coordinates given"""
        return ((self.position[0] - coords[0]) ** 2 +
                (self.position[1] - coords[1]) ** 2 <= self.radius ** 2)

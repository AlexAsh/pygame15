"""Ball logic"""


class Ball:
    """Ball logic"""

    def __init__(self, radius, field):
        self.radius = radius
        self.field = field
        self.position = [0.0, 0.0]
        self.speed = [0.0, 0.0]

    def move(self):
        """Move ball inside field"""
        self.field.move_ball(self)

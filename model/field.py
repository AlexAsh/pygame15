"""Game field logic"""


class Field:
    """Game field logic"""

    def __init__(self, size):
        self.size = map(float, size)

    def get_size(self):
        """Get field size"""
        return self.size

    def move_ball(self, ball):
        ball.position[0] += ball.speed[0]
        ball.position[1] += ball.speed[1]

        if (ball.position[0] + ball.radius >= self.size[0] or
                ball.position[0] - ball.radius <= 0.0):
            ball.speed[0] = -ball.speed[0]

        if (ball.position[1] + ball.radius >= self.size[1] or
                ball.position[1] - ball.radius <= 0.0):
            ball.speed[1] = -ball.speed[1]

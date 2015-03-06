"""Game field logic"""
from model.ball import Ball


class Field:
    """Game field logic"""

    def __init__(self, size):
        self.size = size
        self.ball = None

    def init_ball(self, radius, position, speed):
        """Initialize ball"""
        self.ball = Ball(radius)
        self.ball.position = position
        self.ball.speed = speed

    def move_ball(self, ball):
        """Move ball with it's speed considering borders"""
        ball.position[0] += ball.speed[0]
        ball.position[1] += ball.speed[1]

        if (ball.position[0] + ball.radius >= self.size[0] or
                ball.position[0] - ball.radius <= 0.0):
            ball.speed[0] = -ball.speed[0]

        if (ball.position[1] + ball.radius >= self.size[1] or
                ball.position[1] - ball.radius <= 0.0):
            ball.speed[1] = -ball.speed[1]

    def motion(self):
        """Move object inside field"""
        self.move_ball(self.ball)

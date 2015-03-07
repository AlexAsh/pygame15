"""Game field logic"""
from random import random

from model.ball import Ball


class Field:
    """Game field logic"""

    def __init__(self, size, gravitation):
        self.size = size
        self.gravitation = gravitation
        self.balls = None
        self.frozen = None

    def generate_balls(self, number, radius_range, speed_range):
        """Generate balls"""
        width, height = self.size
        rmin, rmax = radius_range
        vmin, vmax = speed_range

        self.balls = [None] * number
        for i in range(0, number):
            radius = random() * (rmax - rmin) + rmin
            self.balls[i] = Ball(radius)
            self.balls[i].position = [2 * radius + random() * (width - 4 * radius),
                                      2 * radius + random() * (height - 4 * radius)]
            self.balls[i].speed = [vmin + random() * (vmax - vmin),
                                   vmin + random() * (vmax - vmin)]

    def move_ball(self, ball):
        """Move ball with it's speed considering borders"""
        ball.position[0] += ball.speed[0]
        ball.position[1] += ball.speed[1] + self.gravitation / 2.0
        ball.speed[1] += self.gravitation

        if (ball.position[0] + ball.radius >= self.size[0] or
                ball.position[0] - ball.radius <= 0.0):
            ball.speed[0] = -ball.speed[0]

        if (ball.position[1] + ball.radius >= self.size[1] or
                ball.position[1] - ball.radius <= 0.0):
            ball.speed[1] = -ball.speed[1]

    def motion(self):
        """Move object inside field"""
        for ball in self.balls:
            if ball is not self.frozen:
                self.move_ball(ball)

    def freeze(self, coords):
        """Freeze ball by coordinates if any"""
        for ball in self.balls:
            if ball.contains_point(coords):
                self.frozen = ball

    def release(self):
        """Release frozen ball by coordinates if any"""
        self.frozen = None

    def manual_move(self, pos, speed):
        """Move frozen ball manually"""
        if self.frozen:
            self.frozen.position = pos
            self.frozen.speed = speed

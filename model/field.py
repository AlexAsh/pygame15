"""Game field logic"""
from random import random
import math

from model.ball import Ball


class Field:
    """Game field logic"""

    def __init__(self, size, gravitation):
        self.size = size
        self.gravitation = gravitation
        self.balls = None
        self.frozen = None

    def generate_balls(self, number, radius_range, speed_range, rot_range):
        """Generate balls"""
        width, height = self.size
        rmin, rmax = radius_range
        vmin, vmax = speed_range
        rotmin, rotmax = rot_range

        self.balls = [None] * number
        for i in range(0, number):
            radius = random() * (rmax - rmin) + rmin
            self.balls[i] = Ball(radius)
            self.balls[i].position = [2 * radius + random() * (width - 4 * radius),
                                      2 * radius + random() * (height - 4 * radius)]
            self.balls[i].speed = [vmin + random() * (vmax - vmin),
                                   vmin + random() * (vmax - vmin)]
            self.balls[i].rotation_speed = rotmin + random() * (rotmax - rotmin)

    def move_ball(self, ball):
        """Move ball with it's speed considering borders"""
        ball.position[0] += ball.speed[0]
        ball.position[1] += ball.speed[1] + self.gravitation / 2.0
        ball.speed[1] += self.gravitation
        ball.rotated = (ball.rotated + ball.rotation_speed) % 360.0

        if ball.position[0] + ball.radius >= self.size[0]:
            ball.position[0] = self.size[0] - ball.radius
            ball.speed[0] = -abs(ball.speed[0])

        if ball.position[0] - ball.radius <= 0.0:
            ball.position[0] = ball.radius
            ball.speed[0] = abs(ball.speed[0])

        if ball.position[1] + ball.radius >= self.size[1]:
            ball.position[1] = self.size[1] - ball.radius
            ball.speed[1] = -abs(ball.speed[1])

        if ball.position[1] - ball.radius <= 0.0:
            ball.position[1] = ball.radius
            ball.speed[1] = abs(ball.speed[1])

    def motion(self):
        """Move objects inside field"""
        for i in range(0, len(self.balls)):
            for j in range(i + 1, len(self.balls)):
                self.interact_balls(self.balls[i], self.balls[j])

        for ball in self.balls:
            if ball is not self.frozen:
                self.move_ball(ball)

    def interact_balls(self, ball1, ball2):
        """Process interacting balls considering their possible interpenetration"""
        distance_measure = ((ball1.position[0] - ball2.position[0]) ** 2 +
                            (ball1.position[1] - ball2.position[1]) ** 2 -
                            (ball1.radius + ball2.radius) ** 2)

        if distance_measure <= 0:
            self.kick_balls(ball1, ball2)
        if distance_measure < 0:
            self.split_balls(ball1, ball2)

    def kick_balls(self, ball1, ball2):
        """Process kicking balls considering their weights"""
        weight1 = ball1.get_weight()
        weight2 = ball2.get_weight()

        ball1.speed, ball2.speed = (
            map((weight2 / weight1).__mul__, ball2.speed),
            map((weight1 / weight2).__mul__, ball1.speed)
        )

    def split_balls(self, ball1, ball2):
        """Split up interpenetrated balls considering their weights"""
        weight1 = ball1.get_weight()
        weight2 = ball2.get_weight()

        weight_sum = weight1 + weight2
        distance = math.sqrt((ball1.position[0] - ball2.position[0]) ** 2 +
                             (ball1.position[1] - ball2.position[1]) ** 2)
        delta = ball1.radius + ball2.radius - distance
        cos = (ball1.position[0] - ball2.position[0]) / distance
        sin = (ball1.position[1] - ball2.position[1]) / distance
        penetration = [delta * cos, delta * sin]

        ball1.position[0] += penetration[0] * weight2 / weight_sum
        ball2.position[0] -= penetration[0] * weight1 / weight_sum
        ball1.position[1] += penetration[1] * weight2 / weight_sum
        ball2.position[1] -= penetration[1] * weight1 / weight_sum

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

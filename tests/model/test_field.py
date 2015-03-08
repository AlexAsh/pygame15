"""Field model test"""
import math
import unittest

from model.field import Field
from model.ball import Ball


# pylint: disable=too-many-public-methods
class TestField(unittest.TestCase):
    """Field unit test"""

    def setUp(self):
        """Prepare data for test"""
        self.field = Field((640.0, 480), 1.0)
        self.ball1 = None
        self.ball2 = None

    def _set_up_move_ball(self):
        """Prepare data for move ball test"""
        self.ball1 = Ball(10.0)
        self.ball1.position = [320.0, 240.0]
        self.ball1.speed = [0.0, 0.0]

        self.ball2 = Ball(10.0)
        self.ball2.position = [620.0, 460.0]
        self.ball2.speed = [10.0, 10.0]

    def _tear_down_move_ball(self):
        """Erase move ball test data"""
        self.ball1 = None
        self.ball2 = None

    def test_move_ball(self):
        """Test Field move_ball"""
        self._set_up_move_ball()
        self.field.move_ball(self.ball1)
        self.field.move_ball(self.ball2)

        self.assertEqual([320.0, 240.5], self.ball1.position)
        self.assertEqual([0.0, 1.0], self.ball1.speed)
        self.assertEqual([630.0, 470.0], self.ball2.position)
        self.assertEqual([-10.0, -11.0], self.ball2.speed)

        self._tear_down_move_ball()

    def test_generate_balls(self):
        """Test ball generator"""
        number = 3
        radius_range = 20.0, 40.0
        speed_range = 10.0, 30.0
        rot_range = 2.0, 10.0

        self.field.generate_balls(number, radius_range, speed_range, rot_range)
        balls = self.field.balls
        field_size = self.field.size

        self.assertEqual(number, len(balls))
        for i in range(0, number):
            self.assertTrue(
                radius_range[0] <= balls[i].radius <= radius_range[1])
            self.assertTrue(speed_range[0] <= balls[i].speed[0] <= speed_range[1])
            self.assertTrue(speed_range[0] <= balls[i].speed[1] <= speed_range[1])
            self.assertTrue(rot_range[0] <= balls[i].rotation_speed <= rot_range[1])
            self.assertGreater(balls[i].position[0], balls[i].radius)
            self.assertGreater(balls[i].position[1], balls[i].radius)
            self.assertLess(balls[i].position[0], field_size[0] - balls[i].radius)
            self.assertLess(balls[i].position[1], field_size[1] - balls[i].radius)

    class FieldMockMotion(Field):
        """Mock Field class for testing motion method"""
        moved = 0
        interacted = 0

        def move_ball(self, ball):
            """Mock move ball method for testing motion method"""
            self.moved += 1

        def interact_balls(self, ball1, ball2):
            """Mock interact balls method for testing motion method"""
            self.interacted += 1

    def test_motion(self):
        """Test motion with Field mock"""
        balls_number = 4
        field = self.FieldMockMotion(self.field.size, self.field.gravitation)
        field.balls = [Ball(float(i)) for i in range(0, balls_number)]

        field.motion()

        self.assertEqual(balls_number, field.moved)
        self.assertEqual(balls_number * (balls_number - 1) / 2, field.interacted)

    class BallMockFreeze(Ball):
        """Mock Ball class for testing freeze Field method"""
        contains = False

        def contains_point(self, coords):
            """Mock Ball contains method for testing freeze Field method"""
            return self.contains

    def test_freeze(self):
        """Test freeze ball"""
        self.field.balls = [self.BallMockFreeze(10.0), self.BallMockFreeze(10.0)]
        self.field.balls[1].contains = True

        self.field.freeze([0.0, 0.0])
        self.assertTrue(self.field.frozen is self.field.balls[1])

    def test_release(self):
        """Test release ball"""
        self.field.frozen = Ball(10.0)

        self.field.release()
        self.assertTrue(self.field.frozen is None)

    def test_manual_move(self):
        """Test ball manual move"""
        ball = Ball(10.0)
        ball.position = [100.0, 100.0]
        ball.speed = [10.0, 10.0]
        self.field.frozen = ball

        self.field.manual_move([120.0, 150.0], [5.0, 15.0])
        self.assertEqual([120.0, 150.0], self.field.frozen.position)
        self.assertEqual([5.0, 15.0], self.field.frozen.speed)

    class FieldMockInteract(Field):
        """Mock Field class for testing interact balls method"""
        kicked = 0
        split = 0

        def kick_balls(self, ball1, ball2):
            """Mock kick balls method for testing interact balls method"""
            self.kicked += 1

        def split_balls(self, ball1, ball2):
            """Mock split balls method for testing interact balls method"""
            self.split += 1

    def test_interact_balls(self):
        """Test ball interaction method"""
        field = self.FieldMockInteract(self.field.size, self.field.gravitation)

        balls = [Ball(30.0), Ball(20.0), Ball(20.0), Ball(10.0), Ball(50.0), Ball(60.0)]
        balls[0].position = [100.0, 100.0]
        balls[1].position = [130.0, 140.0]
        balls[2].position = [200.0, 200.0]
        balls[3].position = [210.0, 220.0]
        balls[4].position = [300.0, 300.0]
        balls[5].position = [400.0, 400.0]

        field.interact_balls(*balls[0:2])
        field.interact_balls(*balls[2:4])
        field.interact_balls(*balls[4:6])

        self.assertEqual(2, field.kicked)
        self.assertEqual(1, field.split)

    class BallMockGetWeight(Ball):
        """Mock Ball class for testing kick ball/split balls Field methods"""
        weight = 0.0

        def get_weight(self):
            """Mock Ball get weight method for testing kick ball/split balls Field methods"""
            return self.weight

    def test_kick_balls(self):
        """Test kicking balls impulse exchange"""
        ball1, ball2 = self.BallMockGetWeight(10.0), self.BallMockGetWeight(20.0)
        ball1.speed = [10.0, 20.0]
        ball1.weight = 5.0
        ball2.speed = [-10.0, 10.0]
        ball2.weight = 10.0
        ball1_speed_expected = map((ball2.weight / ball1.weight).__mul__, ball2.speed)
        ball2_speed_expected = map((ball1.weight / ball2.weight).__mul__, ball1.speed)

        self.field.kick_balls(ball1, ball2)
        self.assertEqual(ball1_speed_expected, ball1.speed)
        self.assertEqual(ball2_speed_expected, ball2.speed)

    def test_split_balls(self):
        """Test split interpenetrated balls"""
        radius1, radius2 = 30.0, 40.0
        weight1, weight2 = 10.0, 30.0
        pos0 = (100.0, 100.0), (130.0, 140.0)

        distance0 = math.sqrt((pos0[0][0] - pos0[1][0]) ** 2 + (pos0[0][1] - pos0[1][1]) ** 2)
        weight_sum = weight1 + weight2
        tan0 = (pos0[0][0] - pos0[1][0]) / (pos0[0][1] - pos0[1][1])

        balls = self.BallMockGetWeight(radius1), self.BallMockGetWeight(radius2)
        balls[0].position = list(pos0[0])
        balls[0].weight = weight1
        balls[1].position = list(pos0[1])
        balls[1].weight = weight2

        self.field.split_balls(balls[0], balls[1])

        pos = balls[0].position, balls[1].position
        distance = math.sqrt((pos[0][0] - pos[1][0]) ** 2 + (pos[0][1] - pos[1][1]) ** 2)
        tan = (pos[0][0] - pos[1][0]) / (pos[0][1] - pos[1][1])
        moved = (math.sqrt((pos0[0][0] - pos[0][0]) ** 2 + (pos0[0][1] - pos[0][1]) ** 2),
                 math.sqrt((pos0[1][0] - pos[1][0]) ** 2 + (pos0[1][1] - pos[1][1]) ** 2))

        self.assertGreaterEqual(distance, radius1 + radius2)
        self.assertAlmostEqual(moved[0], weight2 / weight_sum * (distance - distance0))
        self.assertAlmostEqual(moved[1], weight1 / weight_sum * (distance - distance0))
        self.assertAlmostEqual(tan, tan0)

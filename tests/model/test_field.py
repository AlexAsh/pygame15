"""Field model test"""
import unittest

from model.field import Field
from model.ball import Ball


# pylint: disable=too-many-public-methods
class TestField(unittest.TestCase):
    """Field unit test"""

    def setUp(self):
        """Prepare data for test"""
        self.field = Field((640.0, 480))
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

        self.assertEqual([320.0, 240.0], self.ball1.position)
        self.assertEqual([630.0, 470.0], self.ball2.position)
        self.assertEqual([-10.0, -10.0], self.ball2.speed)

        self._tear_down_move_ball()

    def test_generate_balls(self):
        """Test ball generator"""
        number = 3
        radius_range = 20.0, 40.0
        speed_range = 10.0, 30.0

        self.field.generate_balls(number, radius_range, speed_range)
        balls = self.field.balls
        field_size = self.field.size

        self.assertEqual(number, len(balls))
        for i in range(0, number):
            self.assertTrue(
                radius_range[0] <= balls[i].radius <= radius_range[1])
            self.assertTrue(speed_range[0] <= balls[i].speed[0] <= speed_range[1])
            self.assertTrue(speed_range[0] <= balls[i].speed[1] <= speed_range[1])
            self.assertGreater(balls[i].position[0], balls[i].radius)
            self.assertGreater(balls[i].position[1], balls[i].radius)
            self.assertLess(balls[i].position[0], field_size[0] - balls[i].radius)
            self.assertLess(balls[i].position[1], field_size[1] - balls[i].radius)

    class FieldMock(Field):
        """Mock Field class for testing motion method"""
        moved = 0

        def move_ball(self, ball):
            """Mock move ball method for testing motion method"""
            self.moved += 1

    def test_motion(self):
        """Test motion with Field mock"""
        balls_number = 7
        field = self.FieldMock(self.field.size)
        field.balls = [Ball(float(i)) for i in range(0, balls_number)]

        field.motion()

        self.assertEqual(balls_number, field.moved)

    class BallMock(Ball):
        """Mock Ball class for testing freeze/release Field methods"""
        contains = False

        def contains_point(self, coords):
            """Mock Ball contains method for testing freeze/release Field methods"""
            return self.contains

    def test_freeze(self):
        """Test freeze ball"""
        self.field.balls = [self.BallMock(10.0), self.BallMock(10.0)]
        self.field.balls[1].contains = True

        self.field.freeze([0.0, 0.0])
        self.assertTrue(self.field.frozen is self.field.balls[1])

    def test_release(self):
        """Test release ball"""
        self.field.frozen = self.BallMock(10.0)

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

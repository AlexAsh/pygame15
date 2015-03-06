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

        self.ball1 = Ball(10.0, self.field)
        self.ball1.position = [320.0, 240.0]
        self.ball1.speed = [0.0, 0.0]

        self.ball2 = Ball(10.0, self.field)
        self.ball2.position = [620.0, 460.0]
        self.ball2.speed = [10.0, 10.0]

    def test_move_ball(self):
        """Test Field move_ball"""
        self.field.move_ball(self.ball1)
        self.field.move_ball(self.ball2)

        self.assertEqual([320.0, 240.0], self.ball1.position)
        self.assertEqual([630.0, 470.0], self.ball2.position)
        self.assertEqual([-10.0, -10.0], self.ball2.speed)

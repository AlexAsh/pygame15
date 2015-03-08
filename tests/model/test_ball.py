"""Ball model test"""
import math
import unittest

from model.ball import Ball


# pylint: disable=too-many-public-methods
class TestBall(unittest.TestCase):
    """Ball unit test"""

    def setUp(self):
        """Prepare data for test"""
        self.ball = Ball(10.0)
        self.ball.position = [30.0, 40.0]

    def test_contains_point(self):
        """Test contains method"""
        self.assertTrue(self.ball.contains_point([35.0, 45.0]))
        self.assertTrue(self.ball.contains_point([24.0, 48.0]))
        self.assertFalse(self.ball.contains_point([35.0, 5.0]))

    def test_get_weight(self):
        """Test Ball weight calculating"""
        self.assertEqual(math.pi * 10.0 ** 2, self.ball.get_weight())

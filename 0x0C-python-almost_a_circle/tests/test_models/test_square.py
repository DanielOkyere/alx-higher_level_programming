#!/usr/bin/python3
"""Unittests for square"""

import unittest
from models.square import Square
from models.base import Base
from models.rectangle import Rectangle


class TestSquare(unittest.TestCase):
    """ Define test for square model"""

    def test_init(self):
        Base._Base__nb_objects = 0
        x = Square(10)
        self.assertEqual(x.id, 1)
        s1 = Square(5, 5, 5, 5)
        self.assertEqual(s1.id, 5)

    def test_init_argument(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float("NaN"))
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(10, float("NaN"))
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(10, 10, float("NaN"))

    def test_attr(self):
        Base._Base__nb_objects = 0
        width_err = "width must be > 0"
        self.assertRaisesRegex(ValueError, width_err, Square, -2)

        x_err = "x must be >= 0"
        self.assertRaisesRegex(ValueError, x_err, Square, 10, -10)
        self.assertRaisesRegex(ValueError, x_err, Square, 10, -100000000000)
        y_err = "y must be >= 0"
        self.assertRaisesRegex(ValueError, y_err, Square, 10, 10, -10)
        self.assertRaisesRegex(ValueError, y_err, Square, 10, 10, -10000000000)

    def test_area(self):
        Base._Base__nb_objects = 0


if __name__ == "__main__":
    unittest.main()

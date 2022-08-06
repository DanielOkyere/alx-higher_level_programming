#!/usr/bin/python3
"""Unittests for base"""

import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangel(unittest.TestCase):
    """Define unit tests for rectangle"""

    def test_init(self):
        r1 = Rectangle(4, 5)
        self.assertEqual(r1.id, Base._Base__nb_objects)

    def test_attr(self):
        Base._Base__nb_objects = 0
        b1 = Rectangle(10, 10, 10, 10, 15)
        self.assertEqual(b1.width, 10)
        self.assertEqual(b1.height, 10)
        self.assertEqual(b1.x, 10)
        self.assertEqual(b1.y, 10)
        self.assertEqual(b1.id, 15)

    def test_attr_validations(self):
        Base._Base__n_objects = 0
        self.assertRaises(TypeError, Rectangle, float("NaN"), float("inf"))
        self.assertRaises(TypeError, Rectangle, float("inf"), float("NaN"))

        w_err = "width must be > 0"
        self.assertRaisesRegex(ValueError, w_err,  Rectangle, -10, -10)


if __name__ == "__main__":
    unittest.main()

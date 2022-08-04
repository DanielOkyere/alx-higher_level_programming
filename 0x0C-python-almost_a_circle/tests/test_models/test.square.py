#!/usr/bin/python3
"""Unittests for square"""

import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """ Define test for square model"""

    def test_init(self):
        s1 = Square(5)
        self.assertEqual(s1.id, 5)

    def test_init_argument(self):
        self.assertRaises(TypeError, Square)


if __name__ == "__main__":
    unittest.main()
    
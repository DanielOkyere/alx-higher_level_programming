#!/usr/bin/python3
import unittest
from models.base import Base


class BaseTest(unittest.TestCase):
    """ Assert basic base creation"""
    def test_base_creation(self):
        """test base create"""
        b = Base()
        self.assertTrue(isinstance(b, Base))

    """ Assert null gives 0"""
    def test_zero_id(self):
        """test zero id"""
        Base._Base__nb_objects = 0
        b = Base()
        self.assertEqual(b.id, 1)


if __name__ == "__main__":
    unittest.main()

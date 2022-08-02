#!/usr/bin/python3
"""base geometry class"""


class BaseGeometry():
    """Area of class"""
    def area(self):
        """ area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates an int"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))

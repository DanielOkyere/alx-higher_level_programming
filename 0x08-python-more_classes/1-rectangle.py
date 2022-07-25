#!/usr/bin/python3
"""A rectangle class"""


class Rectangle:
    """This defines a class for the rectangle class
    This class has a private attribute width and height
    The values of width and height should only be integers.
    a `TypeError` exception would be raise if any is not an int
    """
    def __init__(self, width=0, height=0):
        """The init initializes with height at 0, and width at 0
        """
        self.width = width
        self.height = height

        @property
        def width(self):
            """Getter for width"""
            return self.__width

        @width.setter
        def width(self, value):
            """Setter for width"""
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be >= 0")
            self.__width = value

        @property
        def height(self):
            """Getter for height"""
            return self.__height

        @height.setter
        def height(self, value):
            """Setter for height"""
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            if value < 0:
                raise ValueError("height must be >= 0")
            self.__height = value

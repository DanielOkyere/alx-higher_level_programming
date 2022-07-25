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
        if width < 0:
            raise ValueError("width must be >= 0")
        if height < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        self.width = width
        self.height = height

        @property
        def width(self):
            """Getter for width"""
            return self.__width

        @width.setter
        def width(self, width):
            """Setter for width"""
            self.__width = width

        @property
        def height(self):
            """Getter for height"""
            return self.__height

        @height.setter
        def height(self, height):
            """Setter for height"""
            self.__height = height

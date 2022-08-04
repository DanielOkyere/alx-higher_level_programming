#!/usr/bin/python3
"""Defines the class rectangle which inherits from `Base`"""
from models.base import Base



class Rectangle(Base):
    """Class Rectangle inherits properties from Base
    Attributes:
       __width: width of the rectangle
       __height: height of the rectangle
       __x: x attribute
       __y: y attribute
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initialization
        """
        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

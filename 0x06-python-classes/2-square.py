#!/usr/bin/python3
"""A square class definition"""


class Square:
    """ This class defines what a square class
    is.
    Attributes:
        __size (int): size of a square
    """

    __size = 0

    def __init__(self, size=0):
        """initializes the square
           Args:
                size (int): Interger and should
                be greater than 0
           Returns:
                None
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >=0")
            else:
                self.__size = size

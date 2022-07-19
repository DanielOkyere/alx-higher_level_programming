#!/usr/bin/python3
"""Definition for a square"""


class Square:
    """A square with a private
    size
    """
    __size = 0

    def __init__(self, value):
        """
        Args:
             value (num): int value
        """
        self.__size = value

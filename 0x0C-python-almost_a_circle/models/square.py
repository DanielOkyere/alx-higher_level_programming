#!/usr/bin/python3
""" Definition for Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class inherits the attributes of Rectangle
    Attributes:
        size (int): size of the rectangle
        x (int): x value
        y (int): y value
        id (int): default none
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initializer for Square"""
        super().__init__(size, size, x, y, id)
        self.__size = size

    @property
    def size(self) -> int:
        """Size greater"""
        return self.__size

    @size.setter
    def size(self, value: int):
        """size setter"""
        self.__size = value
        self.width = self.height = value

    def __str__(self) -> str:
        """String representation"""
        id = self.id
        size = self.__size
        x = self.x
        y = self.y
        return "[Square] ({}) {}/{} - {}".format(id, x, y, size)

    def update(self, *args, **kwargs):
        """update arguments"""
        attr = ['id', 'size', 'x', 'y']
        if args:
            for atr, numb in zip(attr, args):
                setattr(self, atr, numb)
        elif kwargs:
            for key, value in kwargs.items():
                if key in attr:
                    setattr(self, key, value)

    def to_dictionary(self) -> dict:
        """ Square to dictionary """
        id = self.id
        size = self.__size
        x = self.x
        y = self.y
        return {'id': id, 'x': x, 'size': size, 'y': y}

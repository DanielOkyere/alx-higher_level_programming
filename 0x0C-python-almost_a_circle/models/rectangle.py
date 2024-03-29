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

    def __str__(self) -> str:
        """string representation
        """
        return "[Rectangle] ({}) {}/{} - {}/{}"\
            .format(self.id, self.x, self.y, self.width, self.height)

    def check_type_value(self, name: str, value: object, greater_equal=False):
        """Validations on types
        """

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if not greater_equal:
            if value <= 0:
                raise ValueError("{} must be > 0".format(name))

        else:
            if value < 0:
                raise ValueError("{} must be >= 0".format(name))

    @property
    def width(self) -> int:
        """width getter
        """
        return self.__width

    @width.setter
    def width(self, width: int):
        """width setter
        """
        self.check_type_value('width', width)
        self.__width = width

    @property
    def height(self) -> int:
        """
        height getter
        """
        return self.__height

    @height.setter
    def height(self, height: int):
        """height setter
        """
        self.check_type_value('height', height)
        self.__height = height

    @property
    def x(self) -> int:
        """x getter
        """
        return self.__x

    @x.setter
    def x(self, x: int):
        """x setter
        """
        self.check_type_value('x', x, True)
        self.__x = x

    @property
    def y(self) -> int:
        """ y getter
        """
        return self.__y

    @y.setter
    def y(self, y: int):
        """Getter for y attribute"""
        self.check_type_value('y', y, True)
        self.__y = y

    def area(self) -> int:
        """area of rectangle"""
        return self.width * self.height

    def display(self):
        """ print # shape"""
        print('\n' * self.y, end='')
        for lh in range(self.height):
            print(' ' * self.x + '#' * self.width)

    def update(self, *args, **kwargs):
        """update rectangle attributes
        """

        expects = (self.id, self.width, self.height, self.x, self.y)
        if args != ():
            self.id, self.width, self.height, self.x, self.y = \
                args + expects[len(args): len(expects)]
        elif kwargs:
            for (name, value) in kwargs.items():
                setattr(self, name, value)

    def to_dictionary(self) -> dict:
        """ Rectangle to dictionary """
        id = self.id
        width = self.width
        height = self.height
        x = self.x
        y = self.y
        return {'x': x, 'width': width, 'id': id, 'height': height,  'y': y}

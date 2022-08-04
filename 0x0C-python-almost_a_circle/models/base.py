#!/usr/bin/python3
"""This defines the base model class"""


class Base:
    """ The base class
    Represents the "base" for all other classes in project
    Atributes:
        __nb_objects (int): The numbr of instatiated Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Initialises the class Base
        Args:
            id(int): The identity of the new Base
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

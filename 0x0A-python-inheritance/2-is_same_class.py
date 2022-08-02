#!/usr/bin/python3
"""Defines a class-checking function"""


def is_same_class(obj, a_class):
    """Checks if an object is exactly an instance of a given class
    Args:
    Obj (any): The object to check
    a_class (type): The class to match the type of obj to.
    Returns:
    If obj is exactly an instance of `a_class` - True.
    otherwise - False
    """
    if type(obj) == a_class:
        return True
    return False

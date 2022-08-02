#!/usr/bin/python3
"""Same is kind of class"""


def is_kind_of_class(obj, a_class):
    """Checks if an object is an instance of a class or not
    Args:
    Obj(any): The object to check
    a_class(type): The class to match the type
    Returns:
    if Obj is an instance or inherited return `True`
    Else return `False`
    """
    if isinstance(obj, a_class):
        return True
    return False

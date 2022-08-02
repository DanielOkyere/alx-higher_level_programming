#!/usr/bin/python3
""" Defines inherits from function"""


def inherits_from(obj, a_class):
    """Inerits details of the class"""
    if issubclass(type(obj), (a_class)) and type(obj) is not a_class:
        return True
    return False

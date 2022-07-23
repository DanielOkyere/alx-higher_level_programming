#!/usr/bin/python3
"""
This is the "0-add_integer" module.

The 0-add_integer module supplies one function, add_integer(a, b).
The numbers suppled must be 2, int or float types and returns an int
"""


def add_integer(a, b):
    """Return the addition of two numbers.
    Otherwise raise a TypeError for a given incorrect argument type.
    """
    h = list(map(lambda x: isinstance(x, (int, float)), [a, b]))

    if all(h):
        return int(a) + int(b)

    for x, y in list(zip(h, ['a', 'b'])):
        if not x:
            raise TypeError("{} must be an integer".format(y))

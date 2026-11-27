#!/usr/bin/python3
"""Module 0-add_integer.

Provides add_integer(), which adds two integers.
"""


def add_integer(a, b=98):
    """Return the sum of a and b as an integer.

    a and b must be integers or floats. Floats are cast to integers
    first. Otherwise a TypeError is raised.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)

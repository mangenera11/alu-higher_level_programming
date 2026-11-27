#!/usr/bin/python3
"""Module 4-print_square.

Provides print_square(), which prints a square with the character #.
"""


def print_square(size):
    """Print a square of size x size using the character #.

    size must be an integer greater than or equal to 0. A TypeError
    is raised for a non-integer and a ValueError for a negative size.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)

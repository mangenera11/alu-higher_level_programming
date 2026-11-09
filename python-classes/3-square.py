#!/usr/bin/python3
"""Module that defines a Square class with size validation and area."""


class Square:
    """A class that defines a square by its size."""

    def __init__(self, size=0):
        """Initialize a square.

        Args:
            size: the size of the square (must be an integer >= 0).

        Raises:
            TypeError: if size is not an integer.
            ValueError: if size is less than 0.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current square area."""
        return self.__size ** 2

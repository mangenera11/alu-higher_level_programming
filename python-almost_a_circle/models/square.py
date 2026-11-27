#!/usr/bin/python3
"""Module square.

Defines the Square class, which inherits from Rectangle.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A square, which is a rectangle with equal width and height."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a Square.

        Args:
            size (int): the size, used as width and height.
            x (int): the x position.
            y (int): the y position.
            id (int): the id, handled by Base.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return [Square] (<id>) <x>/<y> - <size>."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

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

    @property
    def size(self):
        """Get or set the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """Return [Square] (<id>) <x>/<y> - <size>."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """Assign attributes from args, or from kwargs if no args.

        The order of args is id, size, x, y. kwargs are skipped when
        args is not empty.
        """
        attrs = ["id", "size", "x", "y"]
        if args:
            for attr, value in zip(attrs, args):
                setattr(self, attr, value)
        else:
            for key, value in kwargs.items():
                if key in attrs:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of the square."""
        return {"id": self.id, "size": self.size,
                "x": self.x, "y": self.y}

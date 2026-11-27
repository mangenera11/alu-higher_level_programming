#!/usr/bin/python3
"""Module base.

Defines the Base class, which manages the id attribute of all
the other classes in this project.
"""


class Base:
    """Base class that manages id for all other classes."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a Base instance.

        Args:
            id (int): the id to assign. If None, an id is generated
                by incrementing the private class attribute
                __nb_objects.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

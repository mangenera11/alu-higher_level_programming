#!/usr/bin/python3
"""Module that defines the MyList class."""


class MyList(list):
    """A list with a method that prints itself sorted."""

    def print_sorted(self):
        """Print the list in ascending sorted order."""
        print(sorted(self))

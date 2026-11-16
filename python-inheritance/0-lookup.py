#!/usr/bin/python3
"""Module that defines a function to list an object's attributes and methods."""


def lookup(obj):
    """Returns the list of available attributes and methods of an object."""
    return dir(obj)

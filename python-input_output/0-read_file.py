#!/usr/bin/python3
"""Module that defines a function to read a text file."""


def read_file(filename=""):
    """Read a UTF8 text file and print its content to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")

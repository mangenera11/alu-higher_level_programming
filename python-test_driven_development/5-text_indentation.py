#!/usr/bin/python3
"""Module 5-text_indentation.

Provides text_indentation(), which prints text with line breaks.
"""


def text_indentation(text):
    """Print text with 2 new lines after each '.', '?' and ':'.

    There is no space at the beginning or at the end of each printed
    line. text must be a string, otherwise a TypeError is raised.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    result = ""
    for char in text:
        result += char
        if char in ".?:":
            result += "\n\n"
    print("\n".join(line.strip(" ") for line in result.split("\n")), end="")

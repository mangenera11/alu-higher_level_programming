#!/usr/bin/python3
"""Module that defines a Student class that can be saved and reloaded."""


class Student:
    """A student with a first name, last name and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a student.

        Args:
            first_name (str): the first name.
            last_name (str): the last name.
            age (int): the age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return the dictionary description of the student.

        Args:
            attrs (list): if a list of strings, only these attribute
                names are retrieved. Otherwise all attributes are.
        """
        if type(attrs) is list and all(type(a) is str for a in attrs):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace the attributes of the student from a dictionary.

        Args:
            json (dict): attribute names and the values to set.
        """
        for key, value in json.items():
            setattr(self, key, value)

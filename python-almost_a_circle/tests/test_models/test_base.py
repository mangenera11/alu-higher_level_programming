#!/usr/bin/python3
"""Unittests for models/base.py"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test cases for the Base class."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_no_id(self):
        self.assertEqual(Base().id, 1)

    def test_ids_increment(self):
        self.assertEqual(Base().id, 1)
        self.assertEqual(Base().id, 2)
        self.assertEqual(Base().id, 3)

    def test_given_id(self):
        self.assertEqual(Base(12).id, 12)

    def test_given_id_does_not_increment(self):
        Base()
        Base(12)
        self.assertEqual(Base().id, 2)

    def test_zero_id(self):
        self.assertEqual(Base(0).id, 0)

    def test_negative_id(self):
        self.assertEqual(Base(-5).id, -5)

    def test_none_id(self):
        self.assertEqual(Base(None).id, 1)

    def test_string_id(self):
        self.assertEqual(Base("hi").id, "hi")

    def test_nb_objects_is_private(self):
        self.assertFalse(hasattr(Base(), "__nb_objects"))

    def test_too_many_args(self):
        with self.assertRaises(TypeError):
            Base(1, 2)


if __name__ == "__main__":
    unittest.main()

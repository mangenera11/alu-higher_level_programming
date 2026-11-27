#!/usr/bin/python3
"""Unittests for models/square.py"""
import unittest
from io import StringIO
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test cases for the Square class."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def check(self, exc, msg, func, *args):
        with self.assertRaises(exc) as cm:
            func(*args)
        self.assertEqual(str(cm.exception), msg)

    def test_inheritance(self):
        s = Square(3)
        self.assertIsInstance(s, Rectangle)
        self.assertIsInstance(s, Base)

    def test_size_sets_width_and_height(self):
        s = Square(5)
        self.assertEqual((s.width, s.height), (5, 5))

    def test_defaults(self):
        s = Square(5)
        self.assertEqual((s.x, s.y), (0, 0))

    def test_ids(self):
        self.assertEqual(Square(1).id, 1)
        self.assertEqual(Square(1).id, 2)
        self.assertEqual(Square(1, 0, 0, 12).id, 12)

    def test_all_attributes(self):
        s = Square(1, 2, 3, 4)
        self.assertEqual((s.width, s.x, s.y, s.id), (1, 2, 3, 4))

    def test_str(self):
        self.assertEqual(str(Square(5)), "[Square] (1) 0/0 - 5")
        self.assertEqual(str(Square(2, 2, 2, 12)), "[Square] (12) 2/2 - 2")

    def test_area(self):
        self.assertEqual(Square(4).area(), 16)

    def test_display(self):
        with patch("sys.stdout", new=StringIO()) as out:
            Square(2, 1, 1).display()
        self.assertEqual(out.getvalue(), "\n ##\n ##\n")

    def test_size_type(self):
        self.check(TypeError, "width must be an integer", Square, "1")
        self.check(TypeError, "width must be an integer", Square, 1.5)
        self.check(TypeError, "width must be an integer", Square, None)

    def test_size_value(self):
        self.check(ValueError, "width must be > 0", Square, 0)
        self.check(ValueError, "width must be > 0", Square, -3)

    def test_x_validation(self):
        self.check(TypeError, "x must be an integer", Square, 1, "a")
        self.check(ValueError, "x must be >= 0", Square, 1, -1)

    def test_y_validation(self):
        self.check(TypeError, "y must be an integer", Square, 1, 0, "a")
        self.check(ValueError, "y must be >= 0", Square, 1, 0, -1)

    def test_missing_args(self):
        with self.assertRaises(TypeError):
            Square()

    def test_too_many_args(self):
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5)


if __name__ == "__main__":
    unittest.main()

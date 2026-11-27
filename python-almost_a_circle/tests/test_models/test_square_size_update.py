#!/usr/bin/python3
"""Unittests for the size and update methods of Square"""
import unittest
from models.base import Base
from models.square import Square


class TestSquareSize(unittest.TestCase):
    """Test cases for the size getter and setter."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_getter(self):
        self.assertEqual(Square(5).size, 5)

    def test_setter(self):
        s = Square(5)
        s.size = 10
        self.assertEqual((s.size, s.width, s.height), (10, 10, 10))
        self.assertEqual(str(s), "[Square] (1) 0/0 - 10")

    def test_setter_type(self):
        s = Square(5)
        for value in ("9", 2.5, None, [1], {}):
            with self.subTest(value=value):
                with self.assertRaises(TypeError) as cm:
                    s.size = value
                self.assertEqual(str(cm.exception),
                                 "width must be an integer")

    def test_setter_value(self):
        s = Square(5)
        for value in (0, -4):
            with self.subTest(value=value):
                with self.assertRaises(ValueError) as cm:
                    s.size = value
                self.assertEqual(str(cm.exception), "width must be > 0")

    def test_failed_setter_keeps_size(self):
        s = Square(5)
        with self.assertRaises(TypeError):
            s.size = "9"
        self.assertEqual((s.width, s.height), (5, 5))


class TestSquareUpdate(unittest.TestCase):
    """Test cases for Square.update."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_update_args(self):
        s = Square(5)
        s.update(10)
        self.assertEqual(str(s), "[Square] (10) 0/0 - 5")
        s.update(1, 2)
        self.assertEqual(str(s), "[Square] (1) 0/0 - 2")
        s.update(1, 2, 3)
        self.assertEqual(str(s), "[Square] (1) 3/0 - 2")
        s.update(1, 2, 3, 4)
        self.assertEqual(str(s), "[Square] (1) 3/4 - 2")

    def test_update_extra_args_ignored(self):
        s = Square(5)
        s.update(1, 2, 3, 4, 5, 6)
        self.assertEqual(str(s), "[Square] (1) 3/4 - 2")

    def test_update_no_args(self):
        s = Square(5, 1, 2, 3)
        s.update()
        self.assertEqual(str(s), "[Square] (3) 1/2 - 5")

    def test_update_kwargs(self):
        s = Square(5)
        s.update(x=12)
        self.assertEqual(str(s), "[Square] (1) 12/0 - 5")
        s.update(size=7, y=1)
        self.assertEqual(str(s), "[Square] (1) 12/1 - 7")
        s.update(size=7, id=89, y=1)
        self.assertEqual(str(s), "[Square] (89) 12/1 - 7")

    def test_update_kwargs_skipped_when_args(self):
        s = Square(5)
        s.update(10, size=9, x=3)
        self.assertEqual(str(s), "[Square] (10) 0/0 - 5")

    def test_update_unknown_kwarg_ignored(self):
        s = Square(5)
        s.update(color="red")
        self.assertEqual(str(s), "[Square] (1) 0/0 - 5")
        self.assertFalse(hasattr(s, "color"))

    def test_update_validates(self):
        s = Square(5)
        with self.assertRaises(TypeError):
            s.update(1, "a")
        with self.assertRaises(ValueError):
            s.update(size=-1)
        with self.assertRaises(ValueError):
            s.update(1, 2, -3)


if __name__ == "__main__":
    unittest.main()

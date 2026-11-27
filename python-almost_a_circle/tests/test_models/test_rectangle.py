#!/usr/bin/python3
"""Unittests for models/rectangle.py"""
import unittest
from io import StringIO
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle


def _set(obj, name, value):
    setattr(obj, name, value)


class TestRectangleInit(unittest.TestCase):
    """Test cases for creating a Rectangle."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_is_base(self):
        self.assertIsInstance(Rectangle(1, 2), Base)

    def test_ids(self):
        self.assertEqual(Rectangle(10, 2).id, 1)
        self.assertEqual(Rectangle(2, 10).id, 2)
        self.assertEqual(Rectangle(10, 2, 0, 0, 12).id, 12)

    def test_attributes(self):
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual((r.width, r.height, r.x, r.y, r.id),
                         (1, 2, 3, 4, 5))

    def test_defaults(self):
        r = Rectangle(1, 2)
        self.assertEqual((r.x, r.y), (0, 0))

    def test_private_attributes(self):
        r = Rectangle(1, 2, 3, 4)
        self.assertEqual(r._Rectangle__width, 1)
        self.assertEqual(r._Rectangle__height, 2)
        self.assertEqual(r._Rectangle__x, 3)
        self.assertEqual(r._Rectangle__y, 4)

    def test_missing_args(self):
        with self.assertRaises(TypeError):
            Rectangle()
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_too_many_args(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)


class TestRectangleValidation(unittest.TestCase):
    """Test cases for the validation of Rectangle attributes."""

    bad_types = ("2", 2.5, None, [1], {}, (1,), {1})

    def setUp(self):
        Base._Base__nb_objects = 0

    def check(self, exc, msg, func, *args):
        with self.assertRaises(exc) as cm:
            func(*args)
        self.assertEqual(str(cm.exception), msg)

    def test_width_type(self):
        for value in self.bad_types:
            with self.subTest(value=value):
                self.check(TypeError, "width must be an integer",
                           Rectangle, value, 2)

    def test_height_type(self):
        for value in self.bad_types:
            with self.subTest(value=value):
                self.check(TypeError, "height must be an integer",
                           Rectangle, 1, value)

    def test_x_type(self):
        for value in self.bad_types:
            with self.subTest(value=value):
                self.check(TypeError, "x must be an integer",
                           Rectangle, 1, 2, value)

    def test_y_type(self):
        for value in self.bad_types:
            with self.subTest(value=value):
                self.check(TypeError, "y must be an integer",
                           Rectangle, 1, 2, 0, value)

    def test_width_value(self):
        for value in (0, -5):
            with self.subTest(value=value):
                self.check(ValueError, "width must be > 0",
                           Rectangle, value, 2)

    def test_height_value(self):
        for value in (0, -5):
            with self.subTest(value=value):
                self.check(ValueError, "height must be > 0",
                           Rectangle, 1, value)

    def test_x_value(self):
        self.check(ValueError, "x must be >= 0", Rectangle, 1, 2, -1)

    def test_y_value(self):
        self.check(ValueError, "y must be >= 0", Rectangle, 1, 2, 0, -1)

    def test_zero_position_is_valid(self):
        r = Rectangle(1, 2, 0, 0)
        self.assertEqual((r.x, r.y), (0, 0))

    def test_validation_order(self):
        self.check(TypeError, "width must be an integer",
                   Rectangle, "a", "b")
        self.check(TypeError, "height must be an integer",
                   Rectangle, 1, "b", "c")

    def test_setters_validate(self):
        r = Rectangle(1, 2)
        self.check(TypeError, "width must be an integer",
                   _set, r, "width", "a")
        self.check(ValueError, "width must be > 0", _set, r, "width", 0)
        self.check(TypeError, "height must be an integer",
                   _set, r, "height", 1.5)
        self.check(ValueError, "height must be > 0", _set, r, "height", -1)
        self.check(TypeError, "x must be an integer", _set, r, "x", {})
        self.check(ValueError, "x must be >= 0", _set, r, "x", -1)
        self.check(TypeError, "y must be an integer", _set, r, "y", None)
        self.check(ValueError, "y must be >= 0", _set, r, "y", -1)

    def test_setters_assign(self):
        r = Rectangle(1, 2)
        r.width = 10
        r.height = 20
        r.x = 30
        r.y = 40
        self.assertEqual((r.width, r.height, r.x, r.y), (10, 20, 30, 40))

    def test_failed_setter_keeps_value(self):
        r = Rectangle(1, 2)
        with self.assertRaises(ValueError):
            r.width = -1
        self.assertEqual(r.width, 1)


class TestRectangleMethods(unittest.TestCase):
    """Test cases for area, display, __str__ and update."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def output(self, rect):
        with patch("sys.stdout", new=StringIO()) as out:
            rect.display()
        return out.getvalue()

    def test_area(self):
        self.assertEqual(Rectangle(3, 2).area(), 6)
        self.assertEqual(Rectangle(2, 10).area(), 20)
        self.assertEqual(Rectangle(8, 7, 0, 0, 12).area(), 56)

    def test_area_after_change(self):
        r = Rectangle(3, 2)
        r.width = 5
        self.assertEqual(r.area(), 10)

    def test_display(self):
        self.assertEqual(self.output(Rectangle(4, 2)), "####\n####\n")

    def test_display_small(self):
        self.assertEqual(self.output(Rectangle(1, 1)), "#\n")

    def test_display_with_y(self):
        self.assertEqual(self.output(Rectangle(2, 3, 2, 2)),
                         "\n\n  ##\n  ##\n  ##\n")

    def test_display_with_x(self):
        self.assertEqual(self.output(Rectangle(3, 2, 1, 0)),
                         " ###\n ###\n")

    def test_str(self):
        self.assertEqual(str(Rectangle(4, 6, 2, 1, 12)),
                         "[Rectangle] (12) 2/1 - 4/6")

    def test_str_generated_id(self):
        self.assertEqual(str(Rectangle(5, 5, 1)),
                         "[Rectangle] (1) 1/0 - 5/5")

    def test_update_args(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(89)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 10/10")
        r.update(89, 2)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 2/10")
        r.update(89, 2, 3)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 2/3")
        r.update(89, 2, 3, 4)
        self.assertEqual(str(r), "[Rectangle] (89) 4/10 - 2/3")
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_extra_args_ignored(self):
        r = Rectangle(1, 1)
        r.update(5, 2, 3, 4, 5, 6, 7)
        self.assertEqual(str(r), "[Rectangle] (5) 4/5 - 2/3")

    def test_update_no_args(self):
        r = Rectangle(1, 2, 3, 4, 5)
        r.update()
        self.assertEqual(str(r), "[Rectangle] (5) 3/4 - 1/2")

    def test_update_kwargs(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(height=1)
        self.assertEqual(str(r), "[Rectangle] (1) 10/10 - 10/1")
        r.update(width=1, x=2)
        self.assertEqual(str(r), "[Rectangle] (1) 2/10 - 1/1")
        r.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(r), "[Rectangle] (89) 3/1 - 2/1")
        r.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(r), "[Rectangle] (89) 1/3 - 4/2")

    def test_update_kwargs_skipped_when_args(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(89, width=3, x=7)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 10/10")

    def test_update_unknown_kwarg_ignored(self):
        r = Rectangle(1, 2, 3, 4, 5)
        r.update(color="red")
        self.assertEqual(str(r), "[Rectangle] (5) 3/4 - 1/2")
        self.assertFalse(hasattr(r, "color"))

    def test_update_validates(self):
        r = Rectangle(1, 2)
        with self.assertRaises(TypeError):
            r.update(1, "a")
        with self.assertRaises(ValueError):
            r.update(width=-1)


if __name__ == "__main__":
    unittest.main()

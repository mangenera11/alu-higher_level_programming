#!/usr/bin/python3
"""Unittests for to_dictionary and the JSON methods of Base"""
import json
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

FILES = ("Base.json", "Rectangle.json", "Square.json")


def _cleanup():
    for name in FILES:
        if os.path.exists(name):
            os.remove(name)


def _read(name):
    with open(name, "r") as f:
        return f.read()


class SerializationTestCase(unittest.TestCase):
    """Reset the id counter and remove JSON files around each test."""

    def setUp(self):
        Base._Base__nb_objects = 0
        _cleanup()

    def tearDown(self):
        _cleanup()


class TestToDictionary(SerializationTestCase):
    """Test cases for to_dictionary."""

    def test_rectangle(self):
        d = Rectangle(10, 2, 1, 9).to_dictionary()
        self.assertIsInstance(d, dict)
        self.assertEqual(
            d, {"id": 1, "width": 10, "height": 2, "x": 1, "y": 9})

    def test_square(self):
        d = Square(10, 2, 1).to_dictionary()
        self.assertIsInstance(d, dict)
        self.assertEqual(d, {"id": 1, "size": 10, "x": 2, "y": 1})

    def test_rectangle_update_from_dictionary(self):
        r1 = Rectangle(10, 2, 1, 9)
        r2 = Rectangle(1, 1)
        r2.update(**r1.to_dictionary())
        self.assertEqual(str(r1), str(r2))
        self.assertIsNot(r1, r2)
        self.assertNotEqual(r1, r2)

    def test_square_update_from_dictionary(self):
        s1 = Square(10, 2, 1)
        s2 = Square(1, 1)
        s2.update(**s1.to_dictionary())
        self.assertEqual(str(s1), str(s2))
        self.assertIsNot(s1, s2)
        self.assertNotEqual(s1, s2)

    def test_changing_dictionary_keeps_object(self):
        r = Rectangle(1, 2)
        d = r.to_dictionary()
        d["width"] = 99
        self.assertEqual(r.width, 1)


class TestToJsonString(SerializationTestCase):
    """Test cases for Base.to_json_string."""

    def test_none(self):
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_empty_list(self):
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_one_dictionary(self):
        result = Base.to_json_string([{"id": 1}])
        self.assertIsInstance(result, str)
        self.assertEqual(result, '[{"id": 1}]')

    def test_several_dictionaries(self):
        data = [{"id": 1, "x": 2}, {"id": 3, "x": 4}]
        self.assertEqual(json.loads(Base.to_json_string(data)), data)

    def test_rectangle_dictionary(self):
        d = Rectangle(10, 7, 2, 8).to_dictionary()
        self.assertEqual(json.loads(Base.to_json_string([d])), [d])

    def test_missing_argument(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()


class TestFromJsonString(SerializationTestCase):
    """Test cases for Base.from_json_string."""

    def test_none(self):
        self.assertEqual(Base.from_json_string(None), [])

    def test_empty_string(self):
        self.assertEqual(Base.from_json_string(""), [])

    def test_empty_list_string(self):
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_list_of_dictionaries(self):
        data = [{"id": 89, "width": 10, "height": 4},
                {"id": 7, "width": 1, "height": 7}]
        result = Base.from_json_string(Base.to_json_string(data))
        self.assertIsInstance(result, list)
        self.assertEqual(result, data)

    def test_invalid_json(self):
        with self.assertRaises(ValueError):
            Base.from_json_string("[{")

    def test_missing_argument(self):
        with self.assertRaises(TypeError):
            Base.from_json_string()


class TestSaveToFile(SerializationTestCase):
    """Test cases for save_to_file."""

    def test_rectangles(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        self.assertEqual(json.loads(_read("Rectangle.json")),
                         [r1.to_dictionary(), r2.to_dictionary()])

    def test_squares(self):
        s = Square(5, 1, 2)
        Square.save_to_file([s])
        self.assertEqual(json.loads(_read("Square.json")),
                         [s.to_dictionary()])

    def test_none(self):
        Rectangle.save_to_file(None)
        self.assertEqual(_read("Rectangle.json"), "[]")

    def test_empty_list(self):
        Square.save_to_file([])
        self.assertEqual(_read("Square.json"), "[]")

    def test_base_file_name(self):
        Base.save_to_file(None)
        self.assertEqual(_read("Base.json"), "[]")

    def test_overwrites_file(self):
        r1 = Rectangle(1, 1)
        r2 = Rectangle(2, 2)
        Rectangle.save_to_file([r1, r2])
        Rectangle.save_to_file([r2])
        self.assertEqual(json.loads(_read("Rectangle.json")),
                         [r2.to_dictionary()])

    def test_missing_argument(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()


class TestCreate(SerializationTestCase):
    """Test cases for create."""

    def test_rectangle(self):
        r = Rectangle.create(id=89, width=1, height=2, x=3, y=4)
        self.assertIsInstance(r, Rectangle)
        self.assertEqual(str(r), "[Rectangle] (89) 3/4 - 1/2")

    def test_rectangle_defaults(self):
        r = Rectangle.create(id=89, width=1, height=2)
        self.assertEqual(str(r), "[Rectangle] (89) 0/0 - 1/2")

    def test_square(self):
        s = Square.create(id=89, size=1, x=2)
        self.assertIsInstance(s, Square)
        self.assertEqual(str(s), "[Square] (89) 2/0 - 1")

    def test_copy_of_instance(self):
        r1 = Rectangle(3, 5, 1)
        r2 = Rectangle.create(**r1.to_dictionary())
        self.assertEqual(str(r1), str(r2))
        self.assertIsNot(r1, r2)
        self.assertNotEqual(r1, r2)

    def test_invalid_values(self):
        with self.assertRaises(ValueError):
            Rectangle.create(width=-1)
        with self.assertRaises(TypeError):
            Square.create(size="a")


class TestLoadFromFile(SerializationTestCase):
    """Test cases for load_from_file."""

    def test_no_file(self):
        self.assertEqual(Rectangle.load_from_file(), [])
        self.assertEqual(Square.load_from_file(), [])

    def test_empty_list_file(self):
        Rectangle.save_to_file([])
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_rectangles(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        loaded = Rectangle.load_from_file()
        self.assertEqual(len(loaded), 2)
        for obj in loaded:
            self.assertIsInstance(obj, Rectangle)
        self.assertEqual([str(o) for o in loaded], [str(r1), str(r2)])
        self.assertIsNot(loaded[0], r1)
        self.assertIsNot(loaded[1], r2)

    def test_squares(self):
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        Square.save_to_file([s1, s2])
        loaded = Square.load_from_file()
        self.assertEqual(len(loaded), 2)
        for obj in loaded:
            self.assertIsInstance(obj, Square)
        self.assertEqual([str(o) for o in loaded], [str(s1), str(s2)])
        self.assertIsNot(loaded[0], s1)

    def test_class_uses_its_own_file(self):
        Rectangle.save_to_file([Rectangle(1, 1)])
        self.assertEqual(Square.load_from_file(), [])


if __name__ == "__main__":
    unittest.main()

#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer."""

    def test_ordered_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_max_in_middle(self):
        self.assertEqual(max_integer([1, 5, 2]), 5)

    def test_one_element(self):
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_default_argument(self):
        self.assertIsNone(max_integer())

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-5, -2, -9]), -2)

    def test_mixed_signs(self):
        self.assertEqual(max_integer([-1, 0, 1]), 1)

    def test_repeated_max(self):
        self.assertEqual(max_integer([3, 3, 3]), 3)

    def test_floats(self):
        self.assertEqual(max_integer([1.5, 2.5, 0.5]), 2.5)

    def test_int_and_float(self):
        self.assertEqual(max_integer([1, 2.5, 2]), 2.5)

    def test_tuple(self):
        self.assertEqual(max_integer((1, 9, 4)), 9)

    def test_strings(self):
        self.assertEqual(max_integer(["a", "c", "b"]), "c")

    def test_mixed_types(self):
        with self.assertRaises(TypeError):
            max_integer([1, "a"])

    def test_none_argument(self):
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_integer_argument(self):
        with self.assertRaises(TypeError):
            max_integer(5)


if __name__ == "__main__":
    unittest.main()

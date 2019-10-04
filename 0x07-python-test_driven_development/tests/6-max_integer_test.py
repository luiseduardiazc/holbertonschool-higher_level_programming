#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_send_list(self):
        result = max_integer([1, 2, 3, 4])
        self.assertEqual(result, 4)

    def test_empty_list(self):
        result = max_integer([])
        self.assertIsNone(result)

    def test_negative_numbers(self):
        result = max_integer([-50, -10, -5, -2, -1, 0])
        self.assertEqual(result, 0)
        result = max_integer([-50, -10, -5])
        self.assertEqual(result, -5)

    def test_same_numbers(self):
        result = max_integer([200, 200, 200, 200, 200, 200])
        self.assertEqual(result, 200)
        result = max_integer([0, 0, 0, 0])
        self.assertEqual(result, 0)

    def test_float_numbers(self):
        result = max_integer([0.1, 0.2, 0.5, -0.4, 0.02])
        self.assertEqual(result, 0.5)


if __name__ == '__main__':
    unittest.main()

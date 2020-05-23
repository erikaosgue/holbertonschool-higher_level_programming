#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test Max Integer
    Args unittest.TestCase
    """
    def test_value_max(self):
        """Test value max"""
        self.assertEqual(max_integer([3, 2, 1]), 3)

    def test_value_str(self):
        """Test value with str"""
        self.assertEqual(max_integer(["Hello", "World", "No"]), "World")

    def test_value_negative(self):
        """Test value with negative value"""
        self.assertEqual(max_integer([-1, -2, -3]), -1)
        self.assertEqual(max_integer([0, -2, -3]), 0)

    def test_value_float(self):
        """Test value with negative float"""
        self.assertEqual(max_integer([10.0, 10.1, 10.2, 10]), 10.2)

    def test_value_empty(self):
        """Test value with value empty"""
        self.assertEqual(max_integer([]), None)

    def test_without_args(self):
        """Test value with args"""
        self.assertEqual(max_integer(), None)

    def test_value_equal(self):
        """Test value with equal value"""
        self.assertEqual(max_integer([3, 3, 3]), 3)

    def test_value_bool(self):
        """Test value with bool"""
        self.assertEqual(max_integer([True, False]), True)

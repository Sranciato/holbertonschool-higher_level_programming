#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer"""

    def test_correct(self):
        """Test a case with correct values"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_same(self):
        """Test when all of the values are the same"""
        self.assertEqual(max_integer([4, 4, 4, 4]), 4)

    def test_none(self):
        """Test for empty list"""
        self.assertEqual(max_integer([]), None)

    def test_negative(self):
        """Test for negative values"""
        self.assertEqual(max_integer([-3, -5, -6, -30]), -3)

    def test_0_args(self):
        """Test for no arguments"""
        self.assertEqual(max_integer(), None)

    def test_first(self):
        """Test first in list"""
        self.assertEqual(max_integer([100, 2, 4, 5]), 100)

    def test_last(self):
        """Test last in list"""
        self.assertEqual(max_integer([2, 4, 5, 100]), 100)

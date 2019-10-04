#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_correct(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_same(self):
        self.assertEqual(max_integer([4, 4, 4, 4]), 4)

    def test_none(self):
        self.assertEqual(max_integer([]), None)

    def test_negative(self):
        self.assertEqual(max_integer([-3, -5, -6, -30]), -3)

    def test_0_args(self):
        self.assertEqual(max_integer(), None)

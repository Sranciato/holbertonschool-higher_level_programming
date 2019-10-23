#!/usr/bin/python3
"""Module that tests square methods and attributes"""

import pep8
import unittest
import models.base
import models.rectangle
import models.square

Square = models.square.Square
Rectangle = models.rectangle.Rectangle
Base = models.base.Base


class SquareTest(unittest.TestCase):
    """Test for square"""

    def setUp(self):
        """setup assertEquals"""

        self.ae = self.assertEqual

    @classmethod
    def tearDownClass(cls):
        """tear down class"""
        del cls
        pass

    def test_value_square(self):
        """test normal values"""

        s1 = Square(2, 3, 4)

        self.ae(s1.size, 2)
        self.ae(s1.x, 3)
        self.ae(s1.y, 4)

    def test_typeerror(self):
        """test for typeerror"""

        s = Square(1, 1, 1)

        with self.assertRaises(TypeError):
            s.size = "e"

        with self.assertRaises(TypeError):
            s.x = "9"

        with self.assertRaises(TypeError):
            s.y = "5"

    def test_valueerror(self):
        """test for valueerror"""

        s = Square(1, 1, 1)

        with self.assertRaises(ValueError):
            s.size = 0

        with self.assertRaises(ValueError):
            s.x = -3

        with self.assertRaises(ValueError):
            s.y = -2

    def test_area(self):
        """test for area"""

        s = Square(2, 2)
        self.ae(s.area(), 4)

        s2 = Square(5, 0, 0, 13)
        self.ae(s2.area(), 25)

        with self.assertRaises(ValueError):
            s3 = Square(-3, 0, 0)

    def test_pep8_conformance(self):
        """test that we conform to pep8"""

        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["models/square.py"])
        self.ae(result.total_errors, 0,
                "Found code style errors (and warnings).")

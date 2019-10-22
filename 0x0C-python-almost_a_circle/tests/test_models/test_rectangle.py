#!/usr/bin/python3
"""Module that test Rectangle methods and attributes"""

import unittest
import models.base
import models.rectangle

Rectangle = models.rectangle.Rectangle
Base = models.base.Base


class RectangleTest(unittest.TestCase):
    """Test cases for rectangle"""

    def setUp(self):
        """set assertEquals to ae"""

        self.ae = self.assertEqual

    @classmethod
    def tearDownClass(cls):
        """tear down class"""

        pass

    def test_value_rect(self):
        """test normal values"""

        r1 = Rectangle(1, 2, 3, 4)

        self.ae(r1.width, 1)
        self.ae(r1.height, 2)
        self.ae(r1.x, 3)
        self.ae(r1.y, 4)

    def test_typeerror(self):
        """test for typeerror"""

        r = Rectangle(1, 1, 1, 1)

        with self.assertRaises(TypeError):
            r.width = "e"

        with self.assertRaises(TypeError):
            r.height = "4"

        with self.assertRaises(TypeError):
            r.x = "9"

        with self.assertRaises(TypeError):
            r.y = "5"

    def test_valueerror(self):
        """test for valueerror"""

        r = Rectangle(1, 1, 1, 1)

        with self.assertRaises(ValueError):
            r.width = 0

        with self.assertRaises(ValueError):
            r.height = -1

        with self.assertRaises(ValueError):
            r.x = -3

        with self.assertRaises(ValueError):
            r.y = -2

    def test_area(self):
        """test for area"""

        r = Rectangle(4, 2)
        self.ae(r.area(), 8)

        r2 = Rectangle(5, 6, 0, 0, 13)
        self.ae(r2.area(), 30)

    def test_display(self):
        """test for correct display"""

        r = Rectangle(2, 2)
        r.display()

#!/usr/bin/python3
"""Module that tests Base class"""

import unittest
import models.base
import models.rectangle
import models.square
import json

Base = models.base.Base
Rectangle = models.rectangle.Rectangle
Square = models.square.Square


class BaseTest(unittest.TestCase):
    """Tests base.py methods"""

    def setUp(self):
        """Set assertEqual for effiecency"""

        self.ae = self.assertEqual

    @classmethod
    def tearDownClass(cls):
        """called after tests have run"""

        pass

    def test_id(self):
        """test for num of instances"""

        b1 = Base()
        b2 = Base()
        b3 = Base()

        self.ae(b1.id, 1)
        self.ae(b2.id, 2)
        self.ae(b3.id, 3)

    def test_negative(self):
        """test invalid value"""

        try:
            b1 = Base(-2)
        except Exception as e:
            self.ae(print(e), e)

    def test_id_fill(self):
        """test for when base is given an arg"""

        b = Base()
        b2 = Base(7)

        self.ae(b.id, 4)
        self.ae(b2.id, 7)

    def test_to_json(self):
        """test for None and test for normal values"""

        test_dict = {'x': 2, 'width': 10, 'id': 5, 'height': 7, 'y': 8}

        r1 = Rectangle(10, 7, 2, 8, 5)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.ae(dictionary, test_dict)

        json_2 = Base.to_json_string(None)
        self.ae(json_2, "[]")

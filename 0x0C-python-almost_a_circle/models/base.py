#!/usr/bin/python3
"""Base class for all other classes"""
import json
import os


class Base:
    """Base class for other classes"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Class constructor, avoids duplicating the same code"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns json string rep of list of dictionaries"""

        if list_dictionaries is None or len(list_dictionaries) < 1:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the json str representation of list_objs"""

        if list_objs is None:
            list_objs = "[]"

        list_objs = [obj.to_dictionary() for obj in list_objs]
        list_objs = cls.to_json_string(list_objs)
        name = cls.__name__ + ".json"
        with open(name, "wt") as my_file:
            my_file.write(list_objs)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of json string"""

        if json_string is None or len(json_string) < 1:
            return "[]"

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""

        if cls.__name__ == "Rectangle":
            r1 = cls(1, 1)
            r1.update(**dictionary)
            return r1

        if cls.__name__ == "Square":
            s1 = cls(1)
            s1.update(**dictionary)
            return s1

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""

        name = cls.__name__ + ".json"

        if not os.path.exists(name):
            return "[]"

        with open(name, "r") as my_file:
            l = my_file.read()

        objs = cls.from_json_string(l)

        return [cls.create(**o) for o in objs]

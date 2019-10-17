#!/usr/bin/python3
"""Student class"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """instantiation with first, last and age"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves dictionary rep of a Student instance"""

        if type(attrs) is list and type(attrs[0]) is str:
            return {key: v for key, v in vars(self).items() if key in attrs}
        return vars(self)

    def reload_from_json(self, json):
        """replace all attrs of student instance"""

        for k, v in json.items():
            setattr(self, k, v)

#!/usr/bin/python3
"""Class Square that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """calls the logic from rectangle class"""

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """prints formatted string of square"""

        return "[Square] ({}) {}/{} - {}".format(
            self.id,
            self.x,
            self.y,
            self.width
        )

    @property
    def size(self):
        """getter method"""

        return self.width

    @size.setter
    def size(self, value):
        """setter method - sets both width and height to the same value"""

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """assigns attributes"""

        attributes = ("id", "size", "x", "y")
        if len(args) > 0:
            for name, value in zip(attributes, args):
                setattr(self, name, value)
        else:
            for key in kwargs.keys():
                for name in attributes:
                    if key == name:
                        setattr(self, name, kwargs[key])

    def to_dictionary(self):
        """returns dictionary representation of a Rectangle"""

        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }

#!/usr/bin/python3
"""Rectangle class that inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """class constructor for values"""

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """getter method"""

        return self.__width

    @width.setter
    def width(self, value):
        """setter method"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getter method"""

        return self.__height

    @height.setter
    def height(self, value):
        """setter method"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter method"""

        return self.__x

    @x.setter
    def x(self, value):
        """setter method"""

        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getter method"""

        return self.__y

    @y.setter
    def y(self, value):
        """setter method"""

        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """return the area of the rectangle"""

        return self.__width * self.__height

    def display(self):
        """prints rectangle to stdout"""

        for y in range(self.y):
            print()
        for h in range(self.__height):
            print(" " * self.x, end="")
            print("#" * self.__width)

    def __str__(self):
        """prints string to stdout"""

        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id,
            self.x,
            self.y,
            self.width,
            self.height
        )

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""

        attributes = ("id", "width", "height", "x", "y")
        if len(args) > 0:
            i = 0
            for name, value in zip(attributes, args):
                if i == 0:
                    super().__init__(value)
                else:
                    setattr(self, name, value)
                i += 1
        else:
            for key in kwargs.keys():
                for name in attributes:
                    if key == name:
                        setattr(self, name, kwargs[key])

    def to_dictionary(self):
        """returns dictionary representation of a Rectangle"""

        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

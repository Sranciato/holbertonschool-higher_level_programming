#!/usr/bin/python3
"""BaseGeometry class"""


class BaseGeometry:
    """empty class"""

    def area(self):
        """raises exception"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates [value]"""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Rectangle that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """instantiation with width and height"""

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """prints formatted string"""

        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """returns area of rectangle"""

        return self.__width * self.__height


class Square(Rectangle):
    """inherits from rectangle"""

    def __init__(self, size):
        """instantiation with size"""

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """prints formatted string for square"""

        return "[Square] {}/{}".format(self.__size, self.__size)

    def area(self):
        """area of square"""

        return self.__size * self.__size

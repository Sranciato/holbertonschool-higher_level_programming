#!/usr/bin/python3
""" Create a rectangle """


class Rectangle:
    """ A rectangle """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """ initialize values """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ Retrieve width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Set width """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Retrieve height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Set height """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Area of rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ Perimeter of rectangle """
        if self.__height is 0 or self.__width is 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """ Str representation of rectangle """
        new = ""
        if self.__width is 0 or self.__height is 0:
            return new
        for i in range(self.__height):
            new += ((str(self.print_symbol) * self.__width) + "\n")
        return new[:-1]

    def __repr__(self):
        """ Prints repr of rectangle"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """ prints message when instance of Rectangle is deleted """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

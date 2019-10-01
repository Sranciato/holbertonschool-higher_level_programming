#!/usr/bin/python3
"""

Define a square

"""


class Square:
    """Square

    Define a square

    """
    def __init__(self, size=0, position=(0, 0)):
        """ Initialize size and tuple

        Args:
        size
        position

        """
        self.__size = size
        self.position = position

    @property
    def size(self):
        """ returns size """
        return self.__size

    @size.setter
    def size(self, value):
        """ sets size

        args:
        Value: the value to set

        raises:
        TypeError

        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """ returns position """
        return self.__position

    @position.setter
    def position(self, value):
        """ sets position

        args:
        value: the value to set

        raises:
        TypeError

        """
        if type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ Gets area of size

        returns:
        area of square

        """
        return self.__size * self.__size

    def my_print(self):
        """prints square

        print square

        """
        if self.__size == 0:
            print()
        else:
            for p in range(0, self.__position[1]):
                print()
            for i in range(self.__size):
                for pp in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()

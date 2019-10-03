#!/usr/bin/python3
"""Print a square based on size

args: size

"""


def print_square(size):
    """
    Prints a square based on size
    """
    if type(size) != int and type(size) != float:
        raise TypeError("size must be an integer")
    if type(size) == float and size < 0:
        raise TypeError("size must be an integer")
    size = int(size)
    if size < 0:
        raise TypeError("size must be >= 0")

    for i in range(size):
        print("#" * size)

#!/usr/bin/python3
"""Print a square based on size

args: size

"""


def print_square(size):
    """
    Prints a square based on size
    """
    if not isinstance(size, int) and not isinstance(size, float):
        raise TypeError("size must be an integer")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    size = int(size)
    if size < 0:
        raise TypeError("size must be >= 0")

    for i in range(size):
        print("#" * size)

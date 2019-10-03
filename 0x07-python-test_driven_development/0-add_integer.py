#!/usr/bin/python3
"""Add two integers

args: a, b

"""


def add_integer(a, b=98):
    """Adds two integers

    """
    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)

    if type(a) != int:
        raise TypeError("a must be an integer")

    if type(b) != int:
        raise TypeError("b must be an integer")

    return a + b

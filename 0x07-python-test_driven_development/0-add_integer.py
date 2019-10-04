#!/usr/bin/python3
"""Add two integers

args: a, b

"""


def add_integer(a, b=98):
    """Adds two integers

    """
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    if not isinstance(a, int):
        raise TypeError("a must be an integer")

    if not isinstance(b, int):
        raise TypeError("b must be an integer")

    return a + b

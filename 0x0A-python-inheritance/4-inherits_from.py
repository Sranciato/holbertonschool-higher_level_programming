#!/usr/bin/python3
"""Returns true if obj is an instance of a class"""


def inherits_from(obj, a_class):
    """Returns true if obj is an instance of a class"""

    if isinstance(obj, a_class) is True and type(obj) is not a_class:
        return True
    return False

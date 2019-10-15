#!/usr/bin/python3
"""Returns true or false if same instance"""


def is_same_class(obj, a_class):
    """function that checks if object is same"""

    if type(obj) is a_class:
        return True
    if type(obj) is not a_class:
        return False

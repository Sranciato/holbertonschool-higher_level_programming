#!/usr/bin/python3
"""return dictionary description of an object"""


def class_to_json(obj):
    """return dictionary decription of an object"""

    return vars(obj)

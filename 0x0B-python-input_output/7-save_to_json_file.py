#!/usr/bin/python3
"""writes and object to a text file, json representation"""
import json


def save_to_json_file(my_obj, filename):
    """writes and object to a text file, json representation"""

    with open(filename, "w") as myFile:
        json.dump(my_obj, myFile)

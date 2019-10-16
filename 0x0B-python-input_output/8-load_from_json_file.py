#!/usr/bin/python3
"""create an object from json file"""
import json


def load_from_json_file(filename):
    """create and object from a json file"""

    with open(filename, "r") as myFile:
        return json.load(myFile)

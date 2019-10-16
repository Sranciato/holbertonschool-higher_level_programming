#!/usr/bin/python3
"""append string at the end of a text file"""


def append_write(filename="", text=""):
    """append string at the end of a text file"""

    with open(filename, "a+", encoding="utf-8") as myFile:
        return myFile.write(text)

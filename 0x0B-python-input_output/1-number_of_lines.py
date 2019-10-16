#!/usr/bin/python3
"""Returns number of lines of a file"""


def number_of_lines(filename=""):
    """Returns number of lines in file"""

    count = 0
    with open(filename, encoding="utf-8") as myFile:
        for line in myFile:
            count += 1
    return count

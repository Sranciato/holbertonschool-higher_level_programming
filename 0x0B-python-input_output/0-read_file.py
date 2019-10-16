#!/usr/bin/python3
"""Function that opens file and prints to stdout"""


def read_file(filename=""):
    """open file and print to stdout"""

    with open(filename, encoding="utf-8") as myFile:
        print(myFile.read(), end="")

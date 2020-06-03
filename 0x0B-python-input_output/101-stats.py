#!/usr/bin/python3
"""
Reads stdin line by line
"""
import sys


def print_every10():
    """
    prints file size and dictionary of status's
    """
    print("File size: {}".format(file_size))
    for key, value in sorted(dict.items()):
        if (value != 0):
            print("{}: {}".format(key, value))


if __name__ == "__main__":
    num_lines = 1
    file_size = 0
    dict = {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0
        }
    try:
        for line in sys.stdin:
            try:
                status = line.split(" ")[-2]
                size = line.split(" ")[-1]
                file_size += int(size)
            except Exception:
                continue
            if num_lines % 10 == 0:
                print_every10()
            dict[status] += 1
            num_lines += 1

    except KeyboardInterrupt:
        print_every10()
        raise

    print_every10()

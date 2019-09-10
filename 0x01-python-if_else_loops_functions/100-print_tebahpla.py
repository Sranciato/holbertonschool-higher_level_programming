#!/usr/bin/python3
for c in range(122, 96, -1):
    if c % 2 != 0:
        print("{}".format(chr(c - 32)), end="")
    else:
        print("{}".format(chr(c)), end="")

#!/usr/bin/python3
def uppercase(str):
    for char in str:
        new = char
        if ord(char) >= 97 and ord(char) <= 122:
            new = chr(ord(char) - 32)
        print("{}".format(new), end="")
    print("")

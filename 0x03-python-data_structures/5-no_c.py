#!/usr/bin/python3
def no_c(my_string):

    new = ""
    for char in my_string:
        if char == 'c' or char == 'C':
            continue
        new += char
    return new

#!/usr/bin/python3
def value(x):
    if x == 'I':
        return 1
    if x == 'V':
        return 5
    if x == 'X':
        return 10
    if x == 'L':
        return 50
    if x == 'C':
        return 100
    if x == 'D':
        return 500
    if x == 'M':
        return 1000
    return 0


def roman_to_int(roman_string):

    r_str = roman_string
    total = 0
    i = 0

    while i < len(r_str):
        r1 = value(r_str[i])
        if i + 1 < len(r_str):
            r2 = value(r_str[i + 1])
            if r1 >= r2:
                total += r1
                i += 1
            else:
                total += r2 - r1
                i += 2
        else:
            total += r1
            i += 1

    return total

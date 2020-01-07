#!/usr/bin/python3
""" find peak value """


def find_peak(list_of_integers):
    """ function to find peak value in a list """
    lis = list_of_integers
    length = len(lis)

    if lis == []:
        return None
    if length == 1:
        return (lis[0])

    for i in range(0, length - 1):
        if lis[i] > lis[i + 1]:
            return (lis[i])
    return (lis[i + 1])

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
    peak = lis[0]

    for i in range(1, length):
        if lis[i] > peak:
            peak = lis[i]

    return (peak)

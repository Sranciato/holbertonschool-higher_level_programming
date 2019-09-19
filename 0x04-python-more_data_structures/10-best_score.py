#!/usr/bin/python3
def best_score(a_dictionary):

    high = 0
    best = ""

    if a_dictionary is None:
        return None

    for key in a_dictionary.keys():
        if a_dictionary[key] > high:
            best = key
            high = a_dictionary[key]

    return best

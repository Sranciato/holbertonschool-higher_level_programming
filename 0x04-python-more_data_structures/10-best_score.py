#!/usr/bin/python3
def best_score(a_dictionary):

    if a_dictionary is None:
        return None

    high = 0
    best = ""

    for key in a_dictionary.keys():
        if a_dictionary[key] > high:
            best = key
            high = a_dictionary[key]
    if high > 0:
        return best
    return None

#!/usr/bin/python3
def divisible_by_2(my_list=[]):

    new = my_list[:]

    for i in range(len(new)):
        if new[i] % 2 == 0:
            new[i] = True
        else:
            new[i] = False
    return new

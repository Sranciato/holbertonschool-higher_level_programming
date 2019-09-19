#!/usr/bin/python3
def uniq_add(my_list=[]):

    sum = 0
    s = set()

    for i in range(len(my_list)):
        if my_list[i] not in s:
            s.add(my_list[i])
    for i in s:
        sum += i

    return sum

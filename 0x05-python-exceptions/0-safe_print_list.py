#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):

    element = 0

    if x == 0:
        return(0)

    for element in range(0, x):
        try:
            print("{:d}".format(my_list[element]), end="")
        except:
            element -= 1
            break

    element += 1
    print()
    return(element)

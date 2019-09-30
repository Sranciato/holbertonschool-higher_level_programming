#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):

    length = 0

    for element in range(0, x):
        try:
            print("{}".format(my_list[element]), end="")
            length += 1
        except:
            break

    print()
    return(length)

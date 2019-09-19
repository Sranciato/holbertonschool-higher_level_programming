#!/usr/bin/python3
def only_diff_elements(set_1, set_2):

    merge = []
    merge_2 = set()
    set_a = set(set_1)
    set_b = set(set_2)

    merge_2 = set_a & set_b

    merge.extend(set_a)
    merge.extend(set_b)

    for i in merge:
        for x in merge_2:
            if i == x:
                merge.remove(i)

    return merge

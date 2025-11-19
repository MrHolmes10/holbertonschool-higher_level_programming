#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    A=[]
    for i in set_1:
        if i in set_2:
            continue
        else:
            A.append(i)
            continue
    for i in set_2:
        if i in set_1:
            continue
        else:
            A.append(i)
            continue
    return A

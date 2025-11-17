#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    newl = my_list[:]
    if idx < 0 or idx >= len(my_list):
       mylist = my_list
       return mylist
    newl[idx] = element
    return newl

#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    mydi={}
    for i in list(a_dictionary):
         mydi[i]=a_dictionary[i]
    for t in  sorted(mydi):
        print(t,":",mydi[t])

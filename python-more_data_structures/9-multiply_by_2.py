#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    mydi={}
    for i in list(a_dictionary):
         mydi[i]=a_dictionary
    for t in  mydi:
        print(t,": ",mydi[t])

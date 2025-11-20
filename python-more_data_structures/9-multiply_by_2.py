#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    mydi={}
    for i in list(a_dictionary):
         mydi[i]=a_dictionary
    for x in list(mydi):
         mydi[x]=2*mydi[x]
    for t in  mydi:
        print("{}: {}".format(t,mydi[t]))

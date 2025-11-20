#!/usr/bin/python3
def best_score(a_dictionary):
    L=[]
    if a_dictionary != None  :
      for i in a_dictionary:
        L.append(a_dictionary[i])
      return max(L)

#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary != None  :
      a = 0
      for i in a_dictionary:
       t=0
       if a_dictionary[i] > a: 
          a=a_dictionary[i]
          t=i
          keys = [key for key, val in d.items() if val == t] 
      return keys

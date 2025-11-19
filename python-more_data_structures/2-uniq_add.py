#!/usr/bin/python3
def uniq_add(my_list=[]):
   a=[]
   for i in my_list:
       if i in a:
          continue
       else:
          a.append(i)
          continue
   return sum(a)

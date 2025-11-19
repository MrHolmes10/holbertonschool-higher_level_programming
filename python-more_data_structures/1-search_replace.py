#!/usr/bin/python3
def search_replace(my_list, search, replace):
  a=[]
  for i in my_list:
     a.append(i)
     
  for x in range(len(a)):
   if x==search:
     a[x]=replace
    
  return a
 

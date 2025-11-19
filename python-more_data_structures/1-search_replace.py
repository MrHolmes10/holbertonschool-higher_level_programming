#!/usr/bin/python3
def search_replace(my_list, search, replace):
  a=[]
  for i in my_list:
     a.append(i)   
  for x in range(1,len(a)+1):
   if a[x-1]==search:
     a[x-1]=replace
     continue
   else: 
     continue 
  return a
 

#!/usr/bin/python3
def no_c(my_string):
  L=[]
  for i in my_string:
    if i!="C" and i!="c":
      L.append(i)
    else:
       continue
  str="" 
  for k in L:
    str=str+k
 
 print(str)  
  #print("{}".format(str(k)),end="")

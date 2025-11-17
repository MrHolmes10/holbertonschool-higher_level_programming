#!/usr/bin/python3
if  __name__ == "__main__":
 import sys
 L=sys.argv[1:]
 a=1
 if len(L)==0:
  print("0 arguments.")
 elif len(L)==1:
   print("1 argument:")
   print("1: {}".format(L[0]))
 else:
  print("{} arguments:".format(len(L)))
  for i  in L: 
    print("{}: {}".format(a,i))
    a=a+1

#!/usr/bin/python3
if  __name__ == "__main__":
 import sys
 L=sys.argv[1:]
 a=1
 if len(L)==0:
  print("0 argumnets.")
 else:
  print("{} argument:".format(len(L)))
  for i  in L: 
    print("{}: {}".format(a,i))
    a=a+1

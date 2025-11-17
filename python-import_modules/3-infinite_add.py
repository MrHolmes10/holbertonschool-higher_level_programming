#!/usr/bin/python3
if __name__ == "__main__":
 import sys
 l=sys.argv[1:]
 L=[]
 for i  in l:
   i = int(i)
   L.append(i)
 print(sum(L))
 

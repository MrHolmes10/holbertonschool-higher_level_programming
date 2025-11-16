#!/usr/bin/python3
def print_last_digit(n):
  if n>=0:
    l=n%10
  else:
    l=(n*(-1))%10 
 return l
 print(l, end="")

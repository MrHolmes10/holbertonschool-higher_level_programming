#!/usr/bin/python3
def divisible_by_2(my_list=[]):
  resl=my_list[:]
  for i in resl:
   if i%2==0:
     resl[i-1]=True
   else:
     resl[i-1]=False
  return resl

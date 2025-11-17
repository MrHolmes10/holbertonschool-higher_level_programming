#!/usr/bin/python3
def divisible_by_2(my_list=[]):
  resl=my_list[:]
  for i in range(len(resl)):
   if resl[i]%2==0:
     resl[i]=True
   else:
     resl[i]=False
  return resl

#!/usr/bin/python3
def uppercase(str):
 STR=""
 for i in str:
    if ord("a")<=ord(i)<=ord("z"):
       t=ord(i)-(ord("a")-ord("A"))
       STR=STR+chr(t)
    else:
       STR=STR+i
 print(f"{STR}".format(STR))



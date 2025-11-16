#!/usr/bin/python3
def uppercase(str):
 STR=""
 for i in str:
    if ord("A")<=ord(i)<=ord("Z"):
       STR=STR+i
    elif ord("a")<=ord(i)<=ord("z"):
       t=ord(i)-(ord("a")-ord("A"))
       STR=STR+chr(t)
 print(STR)
uppercase("BeSt")

#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    a = 0
    STR=""
    for i in range(x): 
        try:
            s=str(my_list[i])
            STR=STR+s
            a = a + 1
            
        except:
            print(STR,end="")
            print()
            return a
            
    print(STR,end=" ")
    print()
    return a

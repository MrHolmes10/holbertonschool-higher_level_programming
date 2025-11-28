#!/usr/bin/python3
"""tasks 12"""

def pascal_triangle(n):
    """easy !!"""
    try:
        if n <= 0:
            return 0
        L=[[1],[1,1]]
        for x in range(3,n+1):
            T=[1]*x
            for i in range(len(T)):
                try:
                    l=L[x-2]
                    
                    T[i+1]=l[i]+l[i+1]
                    
                
                    continue
                except:
                    try: 
                        T[i]=l[i]+l[i-1]
                        continue
                    except:
                        T[i]=1
                    
                
                L.append(T)       
        for lits in L:
            print(lits)           
    except:
        return 0

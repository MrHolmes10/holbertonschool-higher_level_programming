#!/usr/bin/python3
"""tasks 12"""

def pascal_triangel(n):
    """easyyyy """
    try:
        if n <= 0:
            return 0
        triangle = [[1],[1,1]]
        if n < 3:
            return triangle
                 
        for row in range(3,n+1):
            T=[1]*row
            for i in range(len(T)):
                try:
                    l = triangle[row-2]
                    
                    T[i+1]=l[i]+l[i+1]
                    
                
                    continue
                except:
                    try: 
                        T[i]=l[i]+l[i-1]
                        continue
                    except:
                        T[i]=1
                    
                
                triangle.append(T)
        return triangle   
    except:
        return 0

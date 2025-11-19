#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
 new_mat=[]
 for i in matrix:
     a=0
     for k in i:
        t=k**2
        new_mat.append(t)
        a=a+1
 return new_mat

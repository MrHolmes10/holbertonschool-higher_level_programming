#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
 new_mat=matrix[:]
 for i in new_mat:
     a=0
     for k in i:
        t=k**2
        i[a]=t
        a=a+1
 return new_mat

#!/usr/bin/python3
def square_matrix_simple(matrix = []):
 new_mat = []
 for i in matrix:
     a = [x**2 for x in i]
     new_mat.append(a)
 return new_mat

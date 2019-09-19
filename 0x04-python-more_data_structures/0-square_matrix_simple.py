#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return [[row[x]**2 for row in matrix] for x in range(3)]

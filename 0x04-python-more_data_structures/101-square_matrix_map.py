#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    new_list = [list(map(lambda x: x ** 2, row)) for row in matrix]
    return new_list

#!/usr/bin/python3
"""
int: Module 0. Integers addition


"""


def matrix_divided(matrix, div):
    """
    function that divides all elements of a matrix
    """
    new_matrix = []
    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    if not isinstance(matrix, list):
        raise TypeError('matrix must be a matrix (list of lists) \
of integers/floats')
    len_row = len(matrix[0])
    for row in matrix:
        list_div = []
        if len_row != len(row):
            raise TypeError('Each row of the matrix must have the same size')
        for item in row:
            if not isinstance(item, (int, float)):
                raise TypeError('matrix must be a matrix (list of lists) \
of integers/floats')
            list_div.append(round(item / div, 2))
        new_matrix.append(list_div)
    return new_matrix

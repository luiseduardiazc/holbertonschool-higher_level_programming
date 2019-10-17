#!/usr/bin/python3
""" Python - Input/Output """


def pascal_triangle(n):
    """ Returns a list of lists of integers
        representing the Pascal’s triangle of n """
    triangule = [[1], [1, 1]]
    if n <= 0:
        return []
    elif n == 1:
        return [[1]]
    elif n == 2:
        return triangule

    for i in range(1, n - 1):
        row = [1]
        for j in range(0, len(triangule[i])-1):
            row.extend([triangule[i][j] + triangule[i][j+1]])

        row += [1]
        triangule.append(row)
    return triangule

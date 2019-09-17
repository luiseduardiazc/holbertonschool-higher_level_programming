#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for rows in matrix:
        counter = 1
        for colum in rows:
            if counter is not len(rows):
                print("{:d}".format(colum), end=" ")
            else:
                print("{:d}".format(colum), end="")
            counter += 1
        print()

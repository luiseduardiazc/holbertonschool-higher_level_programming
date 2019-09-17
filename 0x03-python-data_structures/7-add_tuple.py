#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 0:
        tuple_a = (0, 0)
    if len(tuple_b) == 0:
        tuple_b = (0, 0)
    if len(tuple_a) < 2:
        tuple_a = list(tuple_a)
        tuple_a.append(0)
        tuple_a = tuple(tuple_a)
    if len(tuple_b) < 2:
        tuple_b = list(tuple_b)
        tuple_b.append(0)
        tuple_b = tuple(tuple_b)

    sum = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return sum

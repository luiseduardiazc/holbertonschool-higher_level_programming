#!/usr/bin/python3
''' Find a peak '''


def find_peak(list_of_integers):
    ''' function that finds a peak in a list of unsorted integers '''
    _len = len(list_of_integers)
    if _len == 0:
        return None
    list_of_integers.sort()
    return list_of_integers[_len - 1]

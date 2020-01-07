#!/usr/bin/python3
''' Find a peak '''


def find_peak(list_of_integers):
    ''' function that finds a peak in a list of unsorted integers '''
    _len = len(list_of_integers)
    if _len == 0:
        return None
    if _len == 1:
        return list_of_integers[0]
    if list_of_integers[0] > list_of_integers[_len - 1]:
        del list_of_integers[_len - 1]
    else:
        del list_of_integers[0]
    return find_peak(list_of_integers)

#!/usr/bin/python3
''' Find a peak '''


def merge(L1, L2, Li):
    '''
    Merge two sorted python list L1 and L2
    into properly sized list Li
    '''
    i = j = 0
    while i + j < len(Li):
        if j == len(L2) or (i < len(L1) and L1[i] < L2[j]):
            Li[i+j] = L1[i]
            i += 1
        else:
            Li[i+j] = L2[j]
            j += 1


def merge_sort(Li):
    '''
    Sort the elements of Python list Li
    using the merge-sort algorithm.
    '''
    n = len(Li)
    if n < 2:
        return Li
    # divide
    mid = n // 2
    L1 = Li[0:mid]
    L2 = Li[mid:n]
    # conquer (with recursion)
    merge_sort(L1)
    merge_sort(L2)
    # merge results
    merge(L1, L2, Li)


def find_peak(list_of_integers):
    ''' function that finds a peak in a list of unsorted integers '''
    if not list_of_integers:
        return None
    merge_sort(list_of_integers)
    return list_of_integers[-1]

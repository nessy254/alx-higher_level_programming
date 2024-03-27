#!/usr/bin/python3
"""
Module contains a function that finds a peak in a list of unsorted integers.
"""
def find_peak(list_of_integers):
    """
    Function that finds a peak in a list of unsorted integers.
    """
    if not list_of_integers:
        return None

    length = len(list_of_integers)
    n = length // 2
    li = list_of_integers

    if (n == length - 1 or li[n] >= li[n + 1]) \
            and (n == 0 or li[n] >= li[n - 1]):
        return li[n]

    if n > 0 and li[n - 1] > li[n]:
        return find_peak(li[:n])

    return find_peak(li[n:])

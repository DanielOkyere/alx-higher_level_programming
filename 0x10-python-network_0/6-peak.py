#!/usr/bin/python3
"""
Find Peak value Interview test
Using binary search implementation
Iteration Model
"""


def find_peak(list_of_integers):
    """
    Finds the peak element
    :param list_of_integers:
    :return: (Int) peak element
    """
    if len(list_of_integers) == 0:
        return
    else:
        left, right = 0, len(list_of_integers) - 1
        while left < right:
            mid = (left + right) // 2
            mid2 = mid + 1
            if list_of_integers[mid] < list_of_integers[mid2]:
                left = mid2
            else:
                right = mid

        return list_of_integers[left]

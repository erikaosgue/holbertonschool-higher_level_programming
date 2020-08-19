#!/usr/bin/python3
""" Find a peak """


def my_max(list_of_integers):
    """Find the max number of the list"""
    max_value = list_of_integers[0]
    for i in list_of_integers:
        if max_value < i:
            max_value = i
    return max_value


def find_peak(list_of_integers):
    """finds a peak in a list of unsorted integers."""
    if isinstance(list_of_integers, list) and list_of_integers:
        max_value = my_max(list_of_integers)
        return (max_value)
    else:
        return None

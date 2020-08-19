#!/usr/bin/python3
""" Find a peak """


def find_peak(list_of_integers):
    """finds a peak in a list of unsorted integers."""
    if isinstance(list_of_integers, list) and list_of_integers:
        max_value = max(list_of_integers)
        return (max_value)
    else:
        return None

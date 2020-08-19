#!/usr/bin/python3
""" Find a peak """


def find_peak(list_of_integers):
    """finds a max_value in a list of unsorted integers."""
    if not isinstance(list_of_integers, list) or list_of_integers == []:
        return None
    if len(list_of_integers) == 1:
        return list_of_integers[0]
    if len(list_of_integers) == 2:
        if list_of_integers[0] >= list_of_integers[1]:
            return list_of_integers[0]
        else:
            return list_of_integers[1]
    middle = int(len(list_of_integers) / 2)
    max_value = list_of_integers[middle]
    if max_value > list_of_integers[middle - 1] and \
            max_value > list_of_integers[middle + 1]:
        return max_value
    elif max_value < list_of_integers[middle - 1]:
        return find_peak(list_of_integers[:middle])
    else:
        return find_peak(list_of_integers[middle + 1:])

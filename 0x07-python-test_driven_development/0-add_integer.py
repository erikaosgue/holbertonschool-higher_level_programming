#!/usr/bin/python3
""" 0. Integers addition"""


def add_integer(a, b=98):
    """Addition of two integers""""
    if not isinstance(a, (float, int)) or isinstance(a, bool):
        raise TypeError('a must be an integer')

    if not isinstance(b, (float, int)) or isinstance(b, bool):
        raise TypeError('b must be an integer')
    return(int(a) + int(b))

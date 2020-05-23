#!/usr/bin/python3
""" 0. Integers addition
Function that adds 2 integers.
a and b must be integers or floats,
raise a TypeError exception with the a message
a and b must be first casted to integers if they are float"""


def add_integer(a, b=98):
    """Addition of two integers
    Args: a int b an int
    """

    if not isinstance(a, (float, int)) or isinstance(a, bool):
        raise TypeError('a must be an integer')

    elif not isinstance(b, (float, int)) or isinstance(b, bool):
        raise TypeError('b must be an integer')
    a = int(round(a))
    b = int(round(b))
    
    return a + b

#!/usr/bin/python3
"""
    0. Integers addition
    add_integer: that adds 2 integers
    Return: the sum
"""


def add_integer(a, b=98):
    """
        Addition of two integers
        a: int
        b an int
    """

    if not isinstance(a, (int, float)) or isinstance(a, bool):
        raise TypeError("a must be an integer")

    elif not isinstance(b, (int, float)) or isinstance(b, bool):
        raise TypeError("b must be an integer")
    else:
        a = int(round(a))
        b = int(round(b))
    return a + b

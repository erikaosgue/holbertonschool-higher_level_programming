#!/usr/bin/python3
"""
    Integers addition
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

    if not isinstance(b, (int, float)) or isinstance(b, bool):
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b

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

    if a == float("NaN") or b == float("NaN"):
        raise TypeError("b must be an integer")

    if a == float("inf") or a == float("-inf"):
        raise TypeError("b must be an integer")
    if b == float("inf") or b == float("-inf"):
        raise TypeError("b must be an integer")

    sum = a + b
    if sum == float("inf") or sum == float("-inf"):
        raise TypeError("b must be an integer")
    return int(a) + int(b)

#!/usr/bin/python3
"""2. Say my name  a function that prints a square with the character #.

size is the size length of the square
if size is a float and is less than 0,
 raise a TypeError exception with the message size must be an integer"""


def say_my_name(first_name, last_name=""):
    """ Say my name
    Args first name, Last Name
    """

    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    print("My name is {} {}".format(first_name, last_name))

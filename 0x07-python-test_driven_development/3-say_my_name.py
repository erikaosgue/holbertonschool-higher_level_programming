#!/usr/bin/python3
"""
    2. Say my name Module
    Function that prints the first and the last name
    Return: Nothing
"""


def say_my_name(first_name, last_name=""):
    """ Say my name
    Args 
    first_name:the first name
    last_Name: The last name
    """

    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    print("My name is {:s} {:s}".format(first_name, last_name))

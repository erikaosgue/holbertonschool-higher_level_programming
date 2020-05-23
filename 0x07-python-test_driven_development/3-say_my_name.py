#!/usr/bin/python3
"""2. Say my name
Write a function that prints My name is <first name> <last name>

first_name and last_name must be strings otherwise,
raise a TypeError exception with the message first_name must be a string
or last_name must be"""


def say_my_name(first_name, last_name=""):
    """ Say my name
    Args first name, Last Name
    """

    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    print("My name is {:s} {:s}".format(first_name, last_name))

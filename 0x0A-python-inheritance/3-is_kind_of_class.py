#!/usr/bin/python3
"""
    3. Same class or inherit from
    Module: 3-is_kind_of_class.py
"""


def is_kind_of_class(obj, a_class):
    """ Returns True if the object is an
        instance of a class that inherited from
    """
    if isinstance(obj, a_class):
        return True
    return False

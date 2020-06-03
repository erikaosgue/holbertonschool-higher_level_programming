#!/usr/bin/python3
""" 4. Only sub class of
    Module: 4-inherits_from.py
"""


def inherits_from(obj, a_class):
    """ returns True if the object is an instance of a class
        that inherited (directly or indirectly) from the specified class
    """
    if isinstance(obj, a_class):
        if type(obj) is a_class:
            return False
        return True
    return False

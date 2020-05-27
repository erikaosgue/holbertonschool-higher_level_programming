#!/usr/bin/python3
""" 
    31. Low memory cost
    class LockedClass with no class or object attribute,
"""
class LockedClass:
    """ 
        creating new instance attributes
    """
    __slots__ = ["first_name"]

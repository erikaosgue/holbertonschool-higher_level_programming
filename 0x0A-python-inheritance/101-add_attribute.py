#!/usr/bin/python3
"""
    13. Can I?
    modulo: 101-add_attribute.py
"""


def add_attribute(obj, attribute="", name=""):
    """
        function that adds a new attribute to an object
        #if hasattr(obj, '__dict__'): we can use this ption too
        for comparing if it is an instance

    """
    if '__dict__' not in dir(obj):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, name)

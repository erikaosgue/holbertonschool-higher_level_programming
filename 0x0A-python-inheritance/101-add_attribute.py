#!/usr/bin/python3
"""
    13. Can I?
    modulo: 101-add_attribute.py
"""


def add_attribute(obj="", attribute="", name=""):
    """
        function that adds a new attribute to an object
    """
    if str(type(obj)) != "<class '__main__.MyClass'>":
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, name)

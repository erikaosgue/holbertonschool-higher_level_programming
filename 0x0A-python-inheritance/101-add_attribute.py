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
    if attribute == "" or name == "" or obj == "":
        raise TypeError("can't add new attribute")
    if type(attribute) is not str or type(name) is not str:
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, name)

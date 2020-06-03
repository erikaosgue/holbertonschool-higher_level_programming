#!/usr/bin/python3
"""
    10. Class to JSON
    module: 10-class_to_json.py
"""

def class_to_json(obj):
    """class_to_json adds all arguments to a Python list
    Args:
        obj (object): object to add
    """
    return(obj.__dict__)

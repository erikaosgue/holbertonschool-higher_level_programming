#!/usr/bin/python3
""" 6. From JSON string to Object
    module: 6-from_json_string.py
"""
import json


def from_json_string(my_str):
    """from_json_string  returns an object repr. by Json string

    Args:
        my_str (str): string to convert to object
    """
    return(json.loads(my_str))

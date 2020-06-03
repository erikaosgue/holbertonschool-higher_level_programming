#!/usr/bin/python3
""" 5. To JSON string
    module: 5-to_json_string.py
"""
import json


def to_json_string(my_obj):
    """to_json_string: returns the JSON representation of an object

    Args:
        my_obj ([type]): the object to convert in Json representation
    """
    return(json.dumps(my_obj))

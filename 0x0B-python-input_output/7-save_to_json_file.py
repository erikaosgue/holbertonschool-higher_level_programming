#!/usr/bin/python3
"""
    7. Save Object to a file
    module: 7-save_to_json_file.py
"""
import json


def save_to_json_file(my_obj, filename):
    """
    save_to_json_file  writes an Object to a text file, using JSON

    Args:
        my_obj (object): object to transform in Json string
        filename ([type]):file where the Json string will be saved
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)

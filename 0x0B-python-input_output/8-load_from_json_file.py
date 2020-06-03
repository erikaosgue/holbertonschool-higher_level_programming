#!/usr/bin/python3
"""
    8. Create object from a JSON file
    module: 8-load_from_json_file.py
"""
import json


def load_from_json_file(filename):
    """load_from_json_file: creates an Object from a “JSON file”:

    Args:
        filename (str): Json-File to convert to an objet
    """
    with open(filename, 'r') as f:
        obj = json.load(f)

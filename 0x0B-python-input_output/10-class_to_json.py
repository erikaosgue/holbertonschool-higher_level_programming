#!/usr/bin/python3


def class_to_json(obj):
    """class_to_json adds all arguments to a Python list
    Args:
        obj (object): object to add
    """
    return(obj.__dict__)

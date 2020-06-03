#!/usr/bin/python3
"""
    3. Write to a file
    module: 3-write_file.py
"""


def write_file(filename="", text=""):
    """write_file writes a string to a text file

    Args:
        filename (str): Name of the file to open"".
        text (str): Text to write in the file.
    """
    with open(filename, 'w') as f:
        return(f.write(text))

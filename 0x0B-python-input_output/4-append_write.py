#!/usr/bin/python3
""" 4. Append to a fil
    module: 4-append_write.py
"""


def append_write(filename="", text=""):
    """append_write appends a string at the end of a text file

    Args:
        filename (str): Name of the file to open"".
        text (str): Text to append in the text file.
    """
    with open(filename, 'a') as f:
        return(f.write(text))

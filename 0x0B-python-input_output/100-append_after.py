#!/usr/bin/python3
"""
    15. Search and update
    module: 100-append_after.py
"""


def append_after(filename="", search_string="", new_string=""):
    """append_after: inserts a line of text to a file, after each line
    containing a specific string

    Args:
        filename (str): name of the file
        search_string (str) string to find in the file
        new_string (str, optional): string to at after
        finding the search string
    """
    with open(filename, 'r+') as f:
        new_file = ""
        for line in f:
            if search_string in line:
                new_file += line + new_string
            else:
                new_file += line
        f.seek(0)
        f.write(new_file)

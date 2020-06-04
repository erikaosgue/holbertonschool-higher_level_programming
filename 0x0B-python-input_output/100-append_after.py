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
        lines = f.readlines()
        for i, line in enumerate(lines):
            if search_string in line:
                lines[i] = lines[i].strip() + '\n' + new_string
        f.seek(0)
        for line in lines:
            f.write(line)

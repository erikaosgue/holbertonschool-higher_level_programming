#!/usr/bin/python3
""" 1. Number of lines
    modulo: 1-number_of_lines.py
"""


def number_of_lines(filename=""):
    """
    number_of_lines: returns the number of lines of a text file

    Args:
        filename (str): Name of the file to open
    """
    count = 0
    with open(filename) as f:
        for line in f:
            count += 1
    f.close()
    return(count)

#!/usr/bin/python3
"""
    2. Read n lines
    module: 2-read_lines.py
"""


def read_lines(filename="", nb_lines=0):
    """ read_lines reads n lines of a text file
        and prints it to stdout

    Args:
        filename (str): Name of the file to read.
        nb_lines (int): Represent the Number of lines to read.
    """

    # is True is nb lines <= 0 False otherwise
    print_all = nb_lines <= 0
    with open(filename, 'r') as f:
        line_num = 1
        for line in f:
            if line_num > nb_lines and not print_all:
                break
            print(line, end="")
            line_num += 1
    # f.close()

#!/usr/bin/python3
""" 0. Read file
    Modulo: 0-read_file.py
"""


def read_file(filename=""):
    """ reads a text file (UTF8) and prints it to stdout:"""
    with open(filename, 'r') as f:
        line = f.read()
        print(line, end="")
        # for line in f:
        #     print(line, end="")
    f.close()

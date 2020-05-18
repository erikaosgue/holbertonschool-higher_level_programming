#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    result = False
    try:
        print("{:d}".format(value))
        result = True
    except Exception as e:
        print("Exception:", e, file=sys.stderr)
    return (result)

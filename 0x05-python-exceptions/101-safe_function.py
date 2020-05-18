#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    result = None
    try:
        result = fct(args[0], args[1])
    except Exception as e:
        print("Exception:", e, file=sys.stderr)
    except ZeroDivisionError as e:
        print("Exception:", e, file=sys.stderr)
    except IndexError as e:
        print("Exception:", e, file=sys.stderr)
    return (result)

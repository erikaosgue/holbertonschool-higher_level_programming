#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv


def main():
    len_argv = len(argv) - 1
    if len_argv == 0:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    op = argv[2]
    if op == '+':
        print("{} + {} = {}".format(a, b, add(a, b)))
        exit(0)
    elif op == '-':
        print("{} - {} = {}".format(a, b, sub(a, b)))
        exit(0)
    elif op == '*':
        print("{} * {} = {}".format(a, b, mul(a, b)))
        exit(0)
    elif op == '/':
        print("{} / {} = {}".format(a, b, div(a, b)))
        exit(0)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)


if __name__ == "__main__":
    main()

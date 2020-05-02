#!/usr/bin/python3
import dis
import calculator_1 #import add, sub, mul, div

def main():
    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, calculator_1.add(a, b)))
    print("{} - {} = {}".format(a, b, calculator_1.sub(a, b)))
    print("{} * {} = {}".format(a, b, calculator_1.mul(a, b)))
    print("{} / {} = {}".format(a, b, calculator_1.div(a, b)))
dis.dis(main)
if __name__ == "__main__":
    main()

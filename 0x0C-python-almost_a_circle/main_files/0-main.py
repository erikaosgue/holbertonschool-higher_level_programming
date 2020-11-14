#!/usr/bin/python3
""" 0-main """
from models.base import Base

if __name__ == "__main__":

    b1 = Base()
    print(b1.id)

    b2 = Base()
    print(b2.id)

    b3 = Base()
    print(b3.id)

    b4 = Base(12)
    print(b4.id)

    b5 = Base()
    print(b5.id)

    # test cases
    b6 = Base(None)
    print(b6.id)

    b7 = Base("Hello")
    print(b7.id)

    b8 = Base("")
    print(b8.id)

    b9 = Base(-1)
    print(b9.id)

    b10 = Base(1.2)
    print(b10.id)

    # ***
    # b11 = Base(1, 2)
    # print(b11.id)

    b12 = Base([1, 2])
    print(b12.id)

    b13 = Base({1, 2})
    print(b13.id)

    b14 = Base({'A': 1})
    print(b14.id)

    b15 = Base([[1, 2], [3, 4]])
    print(b15.id)

    b17 = Base(float('inf'))
    print(b17.id)

    b18 = Base(float('-inf'))
    print(b18.id)

    b16 = Base(float('nan'))
    print(b16.id)

    b17 = Base(1, 2)
    print(b17.id)


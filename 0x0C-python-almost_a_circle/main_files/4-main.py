#!/usr/bin/python3
""" 4-main """
from models.rectangle import Rectangle
import io
from contextlib import redirect_stdout

if __name__ == "__main__":

    r1 = Rectangle(4, 6)
    r1.display()

    print("---")

    r1 = Rectangle(2, 2)
    r1.display()

    print("---")

    r1 = Rectangle(-1, 2)
    r1.display()

    # f = io.StringIO()
    # with redirect_stdout(f):
    #     r1.display()
    # string = f.getvalue()
    # # print(string)
    # # print('{0}'.format(f.getvalue()), end="")
    # print('{0}'.format(string), end="")
    # print("-----")

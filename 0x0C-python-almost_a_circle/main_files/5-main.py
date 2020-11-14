#!/usr/bin/python3
""" 5-main """
from models.rectangle import Rectangle
import io
from contextlib import redirect_stdout

if __name__ == "__main__":

    r1 = Rectangle(4, 6, 2, 1, 12)
    # print(r1)
    # print(r1.__str__())
    # print(str(r1))

    r2 = Rectangle(5, 5, 1)
    # print(r2)

    f = io.StringIO()
    with redirect_stdout(f):
        print(r1)
    print(f.getvalue(), end="")

    f2 = io.StringIO()
    with redirect_stdout(f):
        print(r2)
    print(f2.getvalue(), end="")
    print(f.getvalue(), f2.getvalue())

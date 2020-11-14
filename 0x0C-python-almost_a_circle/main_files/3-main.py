#!/usr/bin/python3
""" 3-main """
from models.rectangle import Rectangle
import io
from contextlib import redirect_stdout


if __name__ == "__main__":

    r1 = Rectangle(3, 2)
    print(r1.area())
    # 6

    r2 = Rectangle(2, 10)
    print(r2.area())
    # 20

    r3 = Rectangle(8, 7, 0, 0, 12)
    print(r3.area())
    # 56

    f = io.StringIO()
    with redirect_stdout(f):
        print('foobar')
        print(12)
        print("hello")
    print('Got stdout: "{0}, No mas"'.format(f.getvalue()))

    r4 = Rectangle(8, -7, 0, 0, 12)
    print(r4.area())

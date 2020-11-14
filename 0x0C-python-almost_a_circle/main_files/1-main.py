#!/usr/bin/python3
""" 1-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(10, 2)
    print(r1.id)
    # 1

    r2 = Rectangle(2, 10)
    print(r2.id)
    # 2

    r3 = Rectangle(10, 2, 0, 0, 12)
    print(r3.id)
    # 12

    # r4 = Rectangle(1, None, 2)
    # print(r4.id)
    # TypeError: height must be an integer

    # r5 = Rectangle("Hello", 2, 3)
    # print(r5.id)
    # TypeError: width must be an integer

    # r6 = Rectangle(0, 0)
    # print(r7.id)
    # ValueError: width must be > 0

    # r7 = Rectangle(-1, -4, 5, 2)
    # print(r7.id)
    # ValueError: width must be > 0

    # r8 = Rectangle(1.2, 1.3, 1.4)
    # print(r8.id)
    # TypeError: width must be an integer

    # r9 = Rectangle([1, 2], [3, 4])
    # print(r9.id)
    # TypeError: width must be an integer

    # r10 = Rectangle({1, 2}, {3, 4})
    # print(r10.id)
    # TypeError: width must be an integer

    # r11 = Rectangle({'A': 1})
    # print(r11.id)
    # TypeError: width must be an integer

    # r12 = Rectangle([[1, 2], [3, 4]])
    # print(r12.id)
    # TypeError: width must be an integer

    # r13 = Rectangle(True)
    # print(r13.id)
    # TypeError: width must be an integer

    r14 = Rectangle(1, 2, float('nan'), 2)
    print(r14.id)
    # TypeError: x must be an integer

    # r15 = Rectangle(float('inf'), 2)
    # print(r15.id)
    # TypeError: width must be an integer

    # only 1 arg
    # r16 = Rectangle(1)
    # print(r16.id)
    # TypeError: __init__() missing 1 required positional argument: 'height'

    # too many args
    # r17 = Rectangle(1, 2, 3, 4, 5, 6)
    # print(r17.id)
    # TypeError: __init__() takes from 3 to 6 positional arguments but 7 were given

    # missing args
    # r18 = Rectangle()
    # print(r18.id)
    # TypeError: __init__() missing 2 required positional arguments: 'width' and 'height'

    # r19 = Rectangle(-1, True)
    # print(r19.id)
    # ValueError: width must be > 0

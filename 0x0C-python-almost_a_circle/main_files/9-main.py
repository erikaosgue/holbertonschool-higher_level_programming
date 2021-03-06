#!/usr/bin/python3
""" 9-main """
from models.square import Square

if __name__ == "__main__":

    s1 = Square(5)
    print(s1)
    print(s1.area())
    s1.display()

    print("---")

    s2 = Square(2, 2)
    print(s2)
    print(s2.area())
    s2.display()

    print("---")

    s3 = Square(3, 1, 3)
    print(s3)
    print(s3.area())
    s3.display()

    # s4 = Square()
    # print(s4)
    # print(s4.area())
    # s4.display()

    # s5 = Square(1, [2], [3])
    # print(s5)
    # print(s5.area())
    # s5.display()

    # s5 = Square(1, 2, -3)
    # print(s5)
    # print(s5.area())
    # s5.display()

    # s5 = Square(1, "A", -3)
    # print(s5)
    # print(s5.area())
    # s5.display()

    s9 = Square(1, 2, 3, 4, 5, 6)

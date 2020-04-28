#!/usr/bin/python3
def upperletter(i):
        return (i - 32)


def f(i):
        return i if (i % 2 == 0) else upperletter(i)


def main():
        for i in range(122, 96, -1):
                print("{:c}".format(f(i)), end='')
main()

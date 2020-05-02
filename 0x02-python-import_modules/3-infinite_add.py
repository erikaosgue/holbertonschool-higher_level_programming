#!/usr/bin/python3
from sys import argv
import dis

def main():
    sum = 0
    len_argv = len(argv) - 1
    if len_argv == 0:
        print("0")
    else:
        for i in range(1, len_argv + 1):
            sum += int(argv[i])
        print("{}".format(sum))

dis.dis(main)
if __name__ == "__main__":
    main()

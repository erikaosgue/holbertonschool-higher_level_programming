#!/usr/bin/python3
import hidden_4
import sys

if __name__ == "__main__":
    str_ = dir(hidden_4)
    for s in str_:
        if s[:2] != "__":
            print(s)

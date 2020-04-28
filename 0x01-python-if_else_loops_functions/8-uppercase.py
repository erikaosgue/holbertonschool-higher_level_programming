#!/usr/bin/python3
def uppercase(str):
        newstr = ""
        for i in str:
                if ord(i) >= 97 and ord(i) <= 122:
                        newstr += chr(ord(i) - 32)
                else:
                        newstr += i
        print("{:s}".format(newstr))

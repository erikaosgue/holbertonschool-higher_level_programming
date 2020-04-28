#!/usr/bin/python3
def remove_char_at(str, n):
        a = 0
        newstr = ""
        for i in str:
                if a != n:
                        newstr += i
                a += 1
        return (newstr)

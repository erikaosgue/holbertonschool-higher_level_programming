#!/usr/bin/python3
def no_c(my_string):
        new_string = ""
        for char in my_string:
                if (ord(char) == 67 or ord(char) == 99):
                        continue
                else:
                        new_string += char
        return (new_string)

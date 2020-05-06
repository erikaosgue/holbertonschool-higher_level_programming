#!/usr/bin/python3


def max_integer(my_list=[]):
        num = 0
        if len(my_list) == 0:
                return (None)
        for number in my_list:
                if number > num:
                        num = number
                else:
                        continue
        return (num)

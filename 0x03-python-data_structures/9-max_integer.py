#!/usr/bin/python3


def max_integer(my_list=[]):
        num = 0
        for number in my_list:
                if number > num:
                        num = number
                else:
                        continue
        return (num)

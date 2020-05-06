#!/usr/bin/python3

def max_integer(my_list=[]):
        _max = None
        for number in my_list:
                if _max is None or number > _max:
                        _max = number
        return (_max)

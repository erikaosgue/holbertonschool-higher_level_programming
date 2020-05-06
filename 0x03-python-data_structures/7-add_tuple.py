#!/usr/bin/python3


def add_tuple(a, b):
        i = 0
        a_len = len(a)
        b_len = len(b)
        res_len = 2
        res = ()

        for i in range(res_len):
                x, y = 0, 0
                if i < a_len:
                        x = a[i]
                if i < b_len:
                        y = b[i]
                _sum = x + y
                res = res + (_sum,)
        return res

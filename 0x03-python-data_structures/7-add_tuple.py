#!/usr/bin/python3


def add_tuple(a, b):
        a_len = len(a)
        b_len = len(b)
        res_len = min(2, max(a_len, b_len))
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

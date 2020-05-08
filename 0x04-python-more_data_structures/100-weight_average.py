#!/usr/bin/python3
def weight_average(my_list=[]):
    score = 0
    weight = 0
    if my_list:
        for i in my_list:
            score += i[0] * i[1]
            weight += i[1]
        return (score / weight)
    else:
        return 0
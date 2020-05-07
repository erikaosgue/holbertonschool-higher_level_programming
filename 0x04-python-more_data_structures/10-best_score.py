#!/usr/bin/python3


def best_score(a_dictionary):
    new_key = None
    max_num = 0
    if a_dictionary:
        for key, value in a_dictionary.items():
            if value > max_num:
                max_num = value
                new_key = key
    return (new_key)

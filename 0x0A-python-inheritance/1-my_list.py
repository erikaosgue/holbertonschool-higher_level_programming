#!/usr/bin/python3
"""
    1. My list
    A class MyList that inherits from list
"""


class MyList(list):
    """class MyList that inherits from list"""
    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""
        print(sorted(self))
        # new_list = self.copy()
        # new_list.sort()
        # print(new_list)

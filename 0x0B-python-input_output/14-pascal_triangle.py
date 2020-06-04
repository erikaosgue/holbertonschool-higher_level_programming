#!/usr/bin/python3
"""
    14. Pascal's Triangle
    module: 14-pascal_triangle.py
"""


def pascal_triangle(n):
    """pascal_triangle: Creates a Pascal triangle

    Args:
        n (integer):

    Returns:
        A list of lists of integers
    """

    triangle = []
    if n <= 0:
        return triangle
    prev_row = [1]
    triangle.append(prev_row)
    for i in range(1, n):
        row = []
        prev_val = None
        for val in prev_row:
            if prev_val:
                row.append(prev_val + val)
            else:
                row.append(val)
            prev_val = val
        row.append(1)
        triangle.append(row)
        prev_row = row
    return triangle

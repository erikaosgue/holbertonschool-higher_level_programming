#!/usr/bin/python3
""" 1. Divide a matrix
Write a function that prints My name is <first name> <last name>
First_name and last_name must be strings otherwise,
raise a TypeError exception with the message first_name must be a
string or last_name must be a string"""


def matrix_divided(matrix, div):
    """ Matriz of integers divided with div

    """

    msj = 'matrix must be a matrix (list of lists) of integers/floats'

    if not isinstance(matrix, list) or isinstance(matrix, bool):
        raise TypeError(msj)

    if len(matrix) == 0 or not isinstance(matrix[0], list):
        raise TypeError(msj)

    if not matrix[0]:
        raise TypeError(msj)

    row_len = len(matrix[0])
    for row in matrix:
        if not isinstance(row, list) or len(row) != row_len:
            raise TypeError('Each row of the matrix must have the same size')

    for row in matrix:
        for number in row:
            if not isinstance(number, (int, float))\
                    or isinstance(number, bool):
                raise TypeError(msj)

    if not isinstance(div, (int, float)) or isinstance(div, bool):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')

    new_matrix = []
    for row in matrix:
        new_row = []
        for num in row:
            new_row.append(round((num / div), 2))
        new_matrix.append(new_row)
    return (new_matrix)

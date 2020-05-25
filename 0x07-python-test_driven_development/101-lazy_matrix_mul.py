#!/usr/bin/python3
""" 7. Lazy matrix multiplication
A function that multiplies 2 matrices
by using the module NumPy
"""
import numpy


def lazy_matrix_mul(m_a=[], m_b=[]):
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if len(m_a) == 0 or not m_a[0]:
        raise ValueError("m_a can't be empty")

    if len(m_b) == 0 or not m_b[0]:
        raise ValueError("m_b can't be empty")

    if not isinstance(m_a[0], list):
        raise TypeError("m_a must be a list of lists")

    # Testing if row in matix a is a list
    len_row_a = len(m_a[0])
    for row in m_a:
        if not isinstance(row, list):
            raise TypeError("m_a must be a list of lists")
        if len_row_a != len(row):
            raise TypeError("each row of m_a must be of the same size")
        for number in row:
            if not isinstance(number, (int, float)):
                raise TypeError("m_a should contain only integers or floats")

    if not isinstance(m_b[0], list):
        raise TypeError("m_b must be a list of lists")

    # Testing if row in matix b is a list
    len_row_b = len(m_b[0])
    for row in m_b:
        if not isinstance(row, list):
            raise TypeError("m_b must be a list of lists")
        if len_row_b != len(row):
            raise TypeError("each row of m_b must be of the same size")
        for number in row:
            if not isinstance(number, (int, float)):
                raise TypeError("m_b should contain only integers or floats")

    if len_row_a != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    return(numpy.dot(m_a, m_b))

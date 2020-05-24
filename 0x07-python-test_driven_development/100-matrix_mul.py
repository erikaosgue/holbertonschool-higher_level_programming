#!/usr/bin/python3
""" 6. Matrix multiplication

A function that multiplies 2 matrices

"""


def matrix_mul(m_a, m_b):
    """matrix_mul

    Args:
        m_a: Matrix a
        m_b: Matrix b
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if len(m_a) == 0 or not m_a[0]:
        raise ValueError("m_a can't be empty")

    if len(m_b) == 0 or not m_b[0]:
        raise ValueError("m_b can't be empty")

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

    # Testing if row in matix b is a list
    len_colum_b = 0
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

    new_matrix = []
    i = 0
    mul = 0
    for k in range(len(m_a)):
        matrix_row = []
        for j in range(len_row_b):
            for m in range(len_row_a):
                mul += m_a[k][m] * m_b[i][j]
                i += 1
            matrix_row.append(mul)
            i = 0
            mul = 0
        new_matrix.append(matrix_row)
    return (new_matrix)

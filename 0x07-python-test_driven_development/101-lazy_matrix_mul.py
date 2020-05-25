#!/usr/bin/python3
""" 7. Lazy matrix multiplication
A function that multiplies 2 matrices
by using the module NumPy
"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """ Multiplies two matrices using Numpy
        m_a: Matriz a
        m_b: Matriz b
    """
    return(numpy.matmul(m_a, m_b))

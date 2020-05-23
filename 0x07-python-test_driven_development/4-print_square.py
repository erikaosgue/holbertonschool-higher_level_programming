#!/usr/bin/python3
"""
    3. Print square
    print_suquare: a stringa function that prints a square
    Return: nothing
"""

def print_square(size):
    """
        print square by the size
        size
    """

    if isinstance(size, bool):
        raise TypeError('size must be an integer')
    if isinstance(size, float) and size < 0:
        raise TypeError('size must be an integer')
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')

    for i in range(size):
        for j in range(size):
            print('#', end="")
        print()

#!/usr/bin/python3
"""3. Print square a stringa function that prints a square
with the character #.

size is the size length of the square
if size is a float and is less than 0,
 raise a TypeError exception with the message size must be an integer"""


def print_square(size):
    """Print square by the size
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

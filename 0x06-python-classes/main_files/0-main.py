#!/usr/bin/python3
Square = __import__('0-square').Square

my_square = Square()
print(type(my_square))
print(my_square.__dict__)

module = __import__('0-square')
print(module.__doc__)
print(module.Square.__doc__)


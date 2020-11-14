#!/usr/bin/python3
""" 15-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(10, 7, 2, 8)
    r2 = Rectangle(2, 4)
    # Rectangle.save_to_file([r1, r2])
    # Rectangle.save_to_file(None)
    # Rectangle.save_to_file()
    # Rectangle.save_to_file(1, 2)
    # Rectangle.save_to_file("Hello")
    # Rectangle.save_to_file([2, 2.4])

    with open("Rectangle.json", "r") as file:
        print(file.read())

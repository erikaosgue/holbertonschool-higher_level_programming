#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

bg = BaseGeometry()

bg.integer_validator("my_int", 12)
bg.integer_validator("width", 89)

# # bg.integer_validator("", "")
# # bg.integer_validator("width", (1, 2))
# # bg.integer_validator("width", [1, 2])
# # bg.integer_validator("width", True)
# # # bg.integer_validator(1, 2)
# # bg.integer_validator("Hello")
# # bg.integer_validator()
# # bg.integer_validator("Hello", None)
# bg.integer_validator("Hello", {1, 1})
# bg.integer_validator("Hello", -2)


try:
    bg.integer_validator("name", "John")
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    bg.integer_validator("age", 0)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    bg.integer_validator("distance", -4)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))


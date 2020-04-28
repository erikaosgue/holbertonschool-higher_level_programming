#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdigit = 0
flag = 0
str1 = ""
str2 = ""
str1 = "and is greater than 5"
str2 = "and is less than 6 and not 0"
if number < -9:
        number = number * -1
        flag = 1
if number > 9:
        lastdigit = number % 10
else:
        lastdigit = number
if flag:
        number = number * -1
        lastdigit = lastdigit * -1
if lastdigit > 5:
        print("Last digit of", number, "is", lastdigit, str1)
elif lastdigit < 6 and lastdigit != 0:
        print("Last digit of", number, "is", lastdigit, str2)
else:
        print("Last digit of", number, "is", lastdigit, "and is 0")

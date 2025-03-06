#!/usr/bin/python3
import random
number = random.randint(-10, 10)
# YOUR CODE HERE
i = 0
if i > number:
    print(number, "is negative")
elif i < number:
    print(number, "is positive")
else:
    print(number, "is zero")

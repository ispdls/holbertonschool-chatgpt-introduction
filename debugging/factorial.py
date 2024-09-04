#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1  # Decrease n in each iteration to reach the base case (n == 1)
    return result

f = factorial(int(sys.argv[1]))
print(f)
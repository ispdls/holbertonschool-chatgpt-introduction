#!/usr/bin/python3
import sys

if len(sys.argv) < 2:
    print("Usage: python factorial.py <number>")
    sys.exit(1)

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

try:
    f = factorial(int(sys.argv[1]))
    print(f)
except ValueError:
    print("Error: Please provide a valid integer.")
    sys.exit(1)

#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1  # decrement n in each iteration
    return result

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./factorial.py <number>")
        sys.exit(1)

    try:
        num = int(sys.argv[1])
    except ValueError:
        print("Error: Please provide a valid integer.")
        sys.exit(1)

    f = factorial(num)
    print(f)

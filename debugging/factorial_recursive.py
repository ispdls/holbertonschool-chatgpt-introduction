#!/usr/bin/python3
import sys

def factorial(n):
    """
    Computes the factorial of a non-negative integer using recursion.

    The factorial of a non-negative integer n is the product of all positive integers less than or equal to n.
    The factorial of 0 is defined as 1. This function uses recursion to compute the factorial.

    Parameters:
    n (int): A non-negative integer for which the factorial is to be calculated.

    Returns:
    int: The factorial of the integer n. Returns 1 if n is 0.
    
    Example:
    >>> factorial(4)
    24
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Retrieve the integer argument from the command line, compute its factorial, and store the result in `f`.
f = factorial(int(sys.argv[1]))

# Print the computed factorial.
print(f)

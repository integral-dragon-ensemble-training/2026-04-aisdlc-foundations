"""
Simple Calculator Module

This module provides basic arithmetic operations.
Note: Contains intentional bugs for demonstration purposes.
"""


def add(a, b):
    """Add two numbers."""
    return a + b


def subtract(a, b):
    """Subtract b from a."""
    return a - b


def multiply(a, b):
    """Multiply two numbers."""
    return a * b


def divide(a, b):
    """Divide a by b.

    WARNING: This function has a bug!
    It doesn't handle division by zero.
    """
    return a / b


def power(base, exponent):
    """Raise base to the power of exponent."""
    return base ** exponent


def factorial(n):
    """Calculate the factorial of n.

    BUG: This implementation is inefficient and
    doesn't handle negative numbers.
    """
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result = result * i
        return result

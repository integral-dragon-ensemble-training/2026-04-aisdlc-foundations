"""
Main Demo Script

This script demonstrates the calculator and data processor modules.
"""

from calculator import add, subtract, multiply, divide, power, factorial
from data_processor import process_numbers, validate_and_process


def main():
    """Run demo calculations."""
    print("=" * 50)
    print("Calculator Demo")
    print("=" * 50)

    # Basic operations
    print(f"5 + 3 = {add(5, 3)}")
    print(f"10 - 4 = {subtract(10, 4)}")
    print(f"6 * 7 = {multiply(6, 7)}")
    print(f"15 / 3 = {divide(15, 3)}")

    # Power
    print(f"2 ^ 8 = {power(2, 8)}")

    # Factorial
    print(f"5! = {factorial(5)}")

    print("\n" + "=" * 50)
    print("Data Processing Demo")
    print("=" * 50)

    # Process some numbers
    test_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = process_numbers(test_data)

    print(f"Input: {test_data}")
    print(f"Sum: {result['sum']}")
    print(f"Average: {result['average']}")
    print(f"Max: {result['max']}")
    print(f"Min: {result['min']}")
    print(f"Even count: {result['even_count']}")
    print(f"Odd count: {result['odd_count']}")


if __name__ == "__main__":
    main()

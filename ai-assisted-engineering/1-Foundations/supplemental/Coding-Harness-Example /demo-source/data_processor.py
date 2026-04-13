"""
Data Processing Module

This module contains functions for processing lists of numbers.
Note: Code quality could be improved - good refactoring example.
"""


def process_numbers(numbers):
    """Process a list of numbers and return statistics.

    This function is poorly structured and could benefit from
    refactoring - it violates the single responsibility principle.
    """
    # Get the sum
    sum_val = 0
    for n in numbers:
        sum_val = sum_val + n

    # Get the average
    avg_val = sum_val / len(numbers)

    # Get the max
    max_val = numbers[0]
    for n in numbers:
        if n > max_val:
            max_val = n

    # Get the min
    min_val = numbers[0]
    for n in numbers:
        if n < min_val:
            min_val = n

    # Get the count of even numbers
    even_count = 0
    for n in numbers:
        if n % 2 == 0:
            even_count = even_count + 1

    # Get the count of odd numbers
    odd_count = 0
    for n in numbers:
        if n % 2 != 0:
            odd_count = odd_count + 1

    # Return results
    return {
        "sum": sum_val,
        "average": avg_val,
        "max": max_val,
        "min": min_val,
        "even_count": even_count,
        "odd_count": odd_count,
        "total_count": len(numbers)
    }


def validate_and_process(data):
    """Validate data and process it.

    This function tries to do too much - mixing validation,
    transformation, and processing logic.
    """
    # Check if data is a list
    if not isinstance(data, list):
        print("Error: data is not a list")
        return None

    # Check if list is empty
    if len(data) == 0:
        print("Error: data is empty")
        return None

    # Convert all items to numbers and filter out bad data
    numbers = []
    for item in data:
        try:
            num = float(item)
            numbers.append(num)
        except:
            print(f"Warning: Could not convert {item} to number, skipping")

    # Check if we have any valid numbers
    if len(numbers) == 0:
        print("Error: No valid numbers found")
        return None

    # Process the numbers
    result = process_numbers(numbers)
    return result

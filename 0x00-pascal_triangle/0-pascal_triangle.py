#!/usr/bin/python3

"""
This module provides functions to compute the factorial,
combinations, and Pascal's Triangle.

Functions:
    factorial(num: int) -> int
    Computes the factorial of a number.

    combination(n: int, r: int) -> int
    Computes the number of combinations (n choose r).

    pascal_triangle(n: int) -> List[List[int]]
        Generates the first n rows of Pascal's Triangle.
"""


def factorial(num: int) -> int:
    """
    Computes the factorial of a number.

    Args:
        num (int): The number to compute the factorial of.

    Returns:
        int: The factorial of the given number.
    """
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)


def combination(n: int, r: int) -> int:
    """
    Computes the number of combinations (n choose r).

    Args:
        n (int): The total number of items.
        r (int): The number of items to choose.

    Returns:
        int: The number of combinations.
    """
    return factorial(n) // (factorial(r) * factorial(n - r))


def pascal_triangle(n: int):
    """
    Generates the first n rows of Pascal's Triangle.

    Args:
        n (int): The number of rows to generate.

    Returns:
        List[List[int]]: A list of lists representing Pascal's Triangle.
    """
    triangle = []
    for numbers in range(n):
        current_row = []
        for row in range(numbers + 1):
            current_row.append(combination(numbers, row))
        triangle.append(current_row)
    return triangle

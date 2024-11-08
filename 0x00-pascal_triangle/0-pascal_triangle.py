#!/usr/bin/python3

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)


def combination(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))


def pascal_triangle(n) -> int:
    triangle = []
    for numbers in range(n):
        current_row = []
        for row in range(numbers + 1):
            current_row.append(combination(numbers, row))
        triangle.append(current_row)
    return triangle

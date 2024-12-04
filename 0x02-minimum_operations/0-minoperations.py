#!/usr/bin/python3
"""
Calculates the fewest number of operations required to
result in exactly n 'H' characters
in a text file using only two operations: Copy All and Paste.

The algorithm works by finding the prime factorization
of n and using the factors to determine
the minimum number of operations. For each prime factor,
we perform one Copy All and (factor - 1)
Paste operations to accumulate the desired number of
'H' characters.
"""


def minOperations(n):
    """
    Args:
        n (int): The number of 'H' characters to reach in
        the file. n must be a positive integer.

    Returns:
        int: The minimum number of operations needed to
        achieve exactly n 'H' characters.
             If n is impossible to achieve (e.g., if n is 1)
             , returns 0.

    Example:
        minOperations(9)   # Returns: 6
        minOperations(12)  # Returns: 7
        minOperations(1)   # Returns: 0

    Time Complexity:
        O(√n) - The algorithm performs prime factorization,
        which involves checking divisibility up to √n.
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while divisor * divisor <= n:
        while n % divisor == 0:

            operations += divisor
            n //= divisor
        divisor += 1

    if n > 1:
        operations += n

    return operations

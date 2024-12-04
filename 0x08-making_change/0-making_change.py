#!/usr/bin/python3
"""
This module provides a function to determine the
minimum number of coins needed to make a given total.
Functions:
 """


def makeChange(coins, total):
    """
    Determine the minimum number of coins needed to make a given total.
    Args:
        coins (list of int): A list of the values of the available coins.
        total (int): The total amount of money to make change for.
    Returns:
        int: The minimum number of coins needed to make the total, or -1 if
        it is not possible to make the total with the given coins.
    Example:
        >>> makeChange([1, 2, 5], 11)
        3
        >>> makeChange([2], 3)
        -1
    """
    if total <= 0:
        return 0


    dp = [total + 1] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return -1 if dp[total] > total else dp[total]

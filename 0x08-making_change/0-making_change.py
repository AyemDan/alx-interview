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
    if coins == [] or coins is None:
        return -1
    try:
        n = coins.index(total)
        return 1
    except ValueError:
        pass

    coins.sort(reverse=True)
    coin_count = 0
    for i in coins:
        if total % i == 0:
            coin_count += int(total / i)
            return coin_count
        if total - i >= 0:
            if int(total / i) > 1:
                coin_count += int(total / i)
                total = total % i
            else:
                coin_count += 1
                total -= i
                if total == 0:
                    break
    if total > 0:
        return -1
    return coin_count

# Making Change

## Description
This project involves solving the "Making Change" problem, which is a common algorithmic challenge. The goal is to determine the minimum number of coins needed to make a given amount of change from a set of coin denominations.

## Files
- `0-making_change.py`: Contains the function `makeChange(coins, total)` that calculates the minimum number of coins needed to make the given amount of change.

## Function Prototype
```python
def makeChange(coins, total):
    """
    Determines the minimum number of coins needed to make change for a given amount.

    Args:
    coins (list of int): The denominations of the coins available.
    total (int): The total amount of change needed.

    Returns:
    int: The minimum number of coins needed to make the change, or -1 if it is not possible.
    """
```

## Usage
To use the `makeChange` function, import it into your Python script and call it with the appropriate arguments:
```python
from 0-making_change import makeChange

coins = [1, 2, 5]
total = 11
print(makeChange(coins, total))  # Output: 3
```

## Example
Given the coin denominations `[1, 2, 5]` and a total amount of `11`, the minimum number of coins needed is `3` (5 + 5 + 1).

## Author
This project is maintained by Muktr.

## License
This project is licensed under the MIT License.
#!/usr/bin/python3
"""
Determines if all the boxes can be unlocked.
You are given a list of boxes, where each box is a list of keys.
Each key is represented by an integer, which corresponds
to the index of another box that it can unlock.
Initially, you have access to the first box (box 0).
Args:
    boxes (list of list of int): A list of boxes,
    where each box contains a list of keys.
Returns:
    bool: True if all boxes can be unlocked, False otherwise.
"""


def canUnlockAll(boxes):
    """Determines if boxes can be unlocked"""
    unlocked = {0}
    stack = [0]

    while stack:
        current_box = stack.pop()
        for key in boxes[current_box]:
            if key < len(boxes) and key not in unlocked:
                unlocked.add(key)
                stack.append(key)

    return len(unlocked) == len(boxes)

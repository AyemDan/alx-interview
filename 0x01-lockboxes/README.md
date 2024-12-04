# alx-interview
## 0x01. Lockboxes

This project is part of the ALX Interview Preparation curriculum. It involves solving the Lockboxes problem, which is a common algorithmic challenge.

### Description

You have `n` number of locked boxes in front of you. Each box is numbered sequentially from `0` to `n - 1` and each box may contain keys to other boxes. Your goal is to determine if you can open all the boxes starting from box `0`.

### Requirements

- You are given a list of lists `boxes` where `boxes[i]` is a list of keys in the `i-th` box.
- A key with the same number as a box opens that box.
- You can assume all keys will be positive integers.
- The first box `boxes[0]` is initially unlocked.

### Usage

To run the solution, execute the following command:

```bash
python3 lockboxes.py
```

### Example

```python
boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))  # Output: True
```

### Author

Muktr
#!/usr/bin/python3
"""
Define validUTF8(data) function that validates whether a
string of ints represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    Check if a given list of integers represents a valid UTF-8 encoding.
    Args:
        data (list of int): A list of integers where each integer
        represents a byte (0 <= integer <= 255).
    Returns:
        bool: True if the data is a valid UTF-8 encoding, False otherwise.
    The function works by iterating through each byte in the input
    list and checking if it follows the UTF-8 encoding rules:
    - For a single-byte character (0xxxxxxx), the byte starts with '0'.
    - For a multi-byte character, the first byte starts with '110'
    (2 bytes), '1110' (3 bytes), or '11110' (4 bytes).
    - Continuation bytes for multi-byte characters start with '10'.
    """

    continuation_bytes = 0

    for num in data:
        bin_repr = format(num, '08b')

        if continuation_bytes > 0:
            if bin_repr[:2] != '10':
                return False
            continuation_bytes -= 1
        else:
            if bin_repr[:3] == '110':
                continuation_bytes = 1
            elif bin_repr[:4] == '1110':
                continuation_bytes = 2
            elif bin_repr[:5] == '11110':
                continuation_bytes = 3
            elif bin_repr[0] == '0':
                continue
            else:
                return False

    return continuation_bytes == 0

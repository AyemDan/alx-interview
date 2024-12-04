#!/usr/bin/python3
"""Performs log parsing from stdin"""

import re
import sys

counter = 0
file_size = 0
statusC_counter = {200: 0, 301: 0, 400: 0,
                   401: 0, 403: 0, 404: 0, 405: 0, 500: 0}


def printCodes(dict, file_s):
    """Prints the status code and the number of times they appear"""
    print("File size: {}".format(file_s))
    for key in sorted(dict.keys()):
        if dict[key] != 0:
            print("{}: {}".format(key, dict[key]))


if __name__ == "__main__":
    """
    This script reads from standard input line by line and
    parses HTTP log entries.
    It extracts the status code and file size from each
    log entry and keeps track of the total file size and
    the count of each status code.
    The script prints the total file size and the count of
    each status code every 10 lines and upon termination
    (including via keyboard interrupt).
    Functions:
        printCodes(dict, file_s): Prints the total file size
        and the count of each status code in sorted order.
    Variables:
        counter (int): A counter for the number of lines processed.
        file_size (int): The cumulative size of all files processed.
        statusC_counter (dict): A dictionary that maps HTTP
        status codes to their occurrence counts.
    """

    try:
        for line in sys.stdin:
            match = re.search(r'\".*\" (\d{3}) (\d+)', line)
            if match:
                statusC = int(match.group(1))  # Status code
                f_size = int(match.group(2))  # File size
                if statusC in statusC_counter:
                    statusC_counter[statusC] += 1
                file_size += f_size

            counter += 1
            if counter % 10 == 0:
                printCodes(statusC_counter, file_size)

        printCodes(statusC_counter, file_size)

    except KeyboardInterrupt:
        printCodes(statusC_counter, file_size)
        raise

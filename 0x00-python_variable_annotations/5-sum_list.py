#!/usr/bin/env python3
"""task 5"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """task 5"""

    sum = 0
    for item in input_list:
        sum += item
    return sum

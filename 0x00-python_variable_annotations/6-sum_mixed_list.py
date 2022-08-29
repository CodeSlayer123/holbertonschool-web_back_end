#!/usr/bin/env python3
"""task 6"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """task 6"""

    sum = 0
    for item in mxd_lst:
        sum += item
    return sum

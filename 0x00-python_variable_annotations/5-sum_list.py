#!/usr/bin/env python3
from typing import List

def sum_list(input_list: List[float]) -> float:
    sum = 0
    for item in input_list:
        sum += item
    return sum

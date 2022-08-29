#!/usr/bin/env python3
"""task 7"""

from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float], ) -> Tuple[str, float]:
    """task 7"""
    return (k, float(pow(v, 2)))

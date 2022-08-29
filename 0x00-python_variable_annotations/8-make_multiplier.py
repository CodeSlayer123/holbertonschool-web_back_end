#!/usr/bin/env python3
"""task 8"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """task 8"""

    def foo(n: float) -> float:
        """task 8"""
        return n * multiplier
    return foo

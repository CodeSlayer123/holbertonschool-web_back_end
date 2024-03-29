#!/usr/bin/env python3
"""task 1"""
import asyncio
import random
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """task 1"""
    delays = []
    for i in range(n):
        delays.append(asyncio.create_task(wait_random(max_delay)))
    return [await task for task in asyncio.as_completed(delays)]

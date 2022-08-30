#!/usr/bin/env python3
"""task 4"""
import asyncio
import random
wait_random = __import__('0-basic_async_syntax').wait_random
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n, max_delay):
    """task 4"""
    delays = []
    for i in range(n):
        delays.append(task_wait_random(max_delay))
    return [await task for task in asyncio.as_completed(delays)]

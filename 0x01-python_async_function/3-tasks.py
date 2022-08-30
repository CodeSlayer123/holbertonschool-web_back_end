#!/usr/bin/env python3
"""task 3"""
import asyncio
import random
import time
wait_random = __import__('0-basic_async_syntax').wait_random
wait_n = __import__('1-concurrent_coroutines').wait_n


def task_wait_random(max_delay: int) -> asyncio.Task:
    """task 3"""
    return asyncio.create_task(wait_random(max_delay))

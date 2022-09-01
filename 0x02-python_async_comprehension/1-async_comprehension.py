#!/usr/bin/env python3
"""task 1"""
import asyncio
import random
import typing
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> typing.List[float]:
    """task 1"""

    return [i async for i in async_generator()]

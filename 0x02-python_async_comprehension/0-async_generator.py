#!/usr/bin/env python3
"""task 0"""
import asyncio
import random
import typing


async def async_generator() -> typing.Generator[float,
                                                typing.NoneType,
                                                typing.NoneType]:
    """task 0"""

    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

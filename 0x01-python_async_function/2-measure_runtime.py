#!/usr/bin/env python3
#!/usr/bin/env python3
"""task 2"""
import asyncio
import random
import time
wait_random = __import__('0-basic_async_syntax').wait_random
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n, max_delay):
    """task 2"""
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    runtime = end - start
    return runtime / n
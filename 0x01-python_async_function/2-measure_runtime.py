#!/usr/bin/env python3
"""a function that measure time"""

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """A measure time function that takes in 2 integers
       n & max_delay as arguments
    """
    time_begin = time.time()
    asyncio.run(wait_n(n, max_delay))
    time_ends = time.time()
    total_time = time_ends - time_begin
    return total_time / n

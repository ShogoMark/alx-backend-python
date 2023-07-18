#!/usr/bin/env python3

"""coroutine measure_runtime"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
        coroutine that executes async_comprehension 4 times
        in parallel using asyncio.gather
    """
    begin_time = time.time()

    await asyncio.gather(*(async_comprehension() for i in range(4)))

    end_time = time.time()

    total_time = end_time - begin_time

    return total_time

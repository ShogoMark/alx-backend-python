#!/usr/bin/env python3
"""async coroutine that takes in two arguments"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """function spawns the delays n number of times"""
    # creating a list of all tasks
    tasks = [asyncio.create_task(wait_random(max_delay)) for i in range(n)]
    delays = await asyncio.gather(*tasks)

    returns sorted(tasks)

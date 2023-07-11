#!/usr/bin/env python3
"""async coroutine that takes in two arguments"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """function spawns the delays n number of times"""
    # creating a list of all tasks
    tasks = [asyncio.create_task(task_wait_random(max_delay))
             for i in range(n)]
    delays = await asyncio.gather(*tasks)

    return sorted(delays)

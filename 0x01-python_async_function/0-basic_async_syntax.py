#!/usr/bin/env python3
"""async function that takes in delay value and returns it"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
        Async coroutines that waits for a random delay
        time between 0 and max delay and returns it.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

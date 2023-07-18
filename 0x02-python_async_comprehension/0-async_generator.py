#!/usr/bin/env python3
"""A coroutine called async_generator"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
        A coroutine async_generator that yields random numbers
        between 0 and 10 while asynchronously waiting 1 second
    """
    for n in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10

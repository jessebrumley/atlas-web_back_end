#!/usr/bin/env python3
"""
an async routine called wait_n that takes in 2 int arguments (in this order):
n and max_delay. You will spawn wait_random n times w/ the specified max_delay.

wait_n should return the list of all the delays (float values). The list of
the delays should be in ascending order without using sort() because of
concurrency.
"""
import asyncio
import importlib.util
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Calls wait_random n number of times.

    Args:
        n (int): The number of times wait_random is called
        max_delay (int): The maximum delay in seconds. Default is 10.

    Returns:
        list[float]: A list of floats, each returned from wait_random.
    """
    tasks: List[asyncio.Task] = [wait_random(max_delay) for _ in range(n)]

    tasks: List[asyncio.Task] = [wait_random(max_delay) for _ in range(n)]

    results: List[float] = await asyncio.gather(*tasks)

    return sorted(results)

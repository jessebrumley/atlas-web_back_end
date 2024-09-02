#!/usr/bin/env python3
"""
an async routine that takes in 2 int arguments: n and max_delay.
And calls task_wait_random n times w/ the specified max_delay.

task_wait_n should return the list of all the delays (float values).
"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Calls task_wait_random n number of times.

    Args:
        n (int): The number of times wait_random is called
        max_delay (int): The maximum delay in seconds. Default is 10.

    Returns:
        list[float]: A list of floats, each returned from wait_random.
    """
    tasks: List[asyncio.Task] = [task_wait_random(max_delay) for _ in range(n)]

    results: List[float] = await asyncio.gather(*tasks)

    return sorted(results)

#!/usr/bin/env python3
"""
An asynchronous coroutine that takes in an integer argument (max_delay, with a
default value of 10) named wait_random that waits for a random delay between
0 and max_delay seconds and eventually returns it.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronously waits for a random delay between 0 and max_delay seconds.

    Args:
        max_delay (int): The maximum delay in seconds. Default is 10.

    Returns:
        float: The actual delay time in seconds.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

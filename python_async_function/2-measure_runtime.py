#!/usr/bin/env python3
"""
A function measures the total run time for the wait_n function.
"""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total run time for the wait_n function.

    Args:
        n (int): The number of times to call wait_random
        max_delay (int): The max_delay used for wait_random

    Returns:
        list[float]: The average run time per call.
    """
    delays: List[float] = await wait_n(n, max_delay)

    average_delay = sum(delays) / n

    return average_delay

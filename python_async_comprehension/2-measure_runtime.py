#!/usr/bin/env python3
"""
Measure the runtime of executing async_comprehension four times in parallel.
"""
import asyncio
import time
from typing import List

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Executes async_comprehension four times in parallel using asyncio.gather,
    measures the total runtime, and returns it.

    Yields:
        float: The total runtime in seconds.
    """
    start_time = time.time()
    coroutines = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*coroutines)
    end_time = time.time()

    return end_time - start_time

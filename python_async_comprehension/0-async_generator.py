#!/usr/bin/env python3
"""
An asynchronous generator that yields 10 random floating-point numbers
between 0 and 10, each after waiting for 1 second.
"""

import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    An asynchronous generator that yields 10 random floating-point numbers
    between 0 and 10, each after waiting for 1 second.

    Yields:
        float: A random float between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

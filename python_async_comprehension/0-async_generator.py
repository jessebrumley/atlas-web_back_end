"""
An Async Generator. A coroutine that loops 10 times, each time asynchronously
waiting 1 second, and then yields a random number between 0 and 10.
"""

import random
import asyncio

async def async_generator()
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

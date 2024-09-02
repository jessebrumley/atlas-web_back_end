#!/usr/bin/env python3
"""
A  coroutine will collect 10 random numbers using an async comprehensing
over async_generator, then return the 10 random numbers.
"""
import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    A  coroutine will collect 10 random numbers using an async comprehensing
    over async_generator, then return the 10 random numbers.

    Yields:
        list [float]: A list of 10 random floats collected asynchronously.
    """
    numbers = [num async for num in async_generator()]
    return numbers

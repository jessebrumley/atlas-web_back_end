#!/usr/bin/env python3
import asyncio

measure_time = __import__('2-measure_runtime').measure_time

n = 5
max_delay = 9

if __name__ == "__main__":
    result = asyncio.run(measure_time(n, max_delay))
    print(result)

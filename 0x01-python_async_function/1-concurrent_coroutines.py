#!/usr/bin/env python3
"""
Asynchronous routine that spawns wait_random n
times with the specified max_delay.
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    Asynchronous function.
        :param n: Number of times to spawn wait_random.
        :param max_delay: Maximum delay in seconds for wait_random
    """

    delays = [wait_random(max_delay) for _ in range(n)]
    completed = []
    for task in asyncio.as_completed(delays):
        completed.append(await task)

    return completed

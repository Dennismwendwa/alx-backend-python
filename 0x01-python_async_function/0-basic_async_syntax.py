#!/usr/bin/env python3
"""This is asyncio function"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay between 0 and
    max_delay seconds (inclusive).
    """

    random_delay = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay

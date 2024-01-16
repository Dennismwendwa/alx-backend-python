#!/usr/bin/env python3
"""Run time for four parallel comprehensions"""
from asyncio import gather
from time import perf_counter
from typing import List
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Asynchronous coroutine that measures the total runtime for executing
    async_comprehension four times in parallel.
    """
    start_time = perf_counter()
    await gather(
        async_comprehension(), async_comprehension(),
        async_comprehension(), async_comprehension()
    )
    return perf_counter() - start_time

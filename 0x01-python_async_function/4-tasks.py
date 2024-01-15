#!/usr/bin/env python3
"""This function calls asyncio"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Function that returns an asyncio.Task for wait_random"""
    return asyncio.create_task(wait_random(max_delay))


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    """Asynchronous routine that spawns task_wait_random n times"""

    tasks = [task_wait_random(max_delay) for _ in range(n)]
    completed = []

    for task in asyncio.as_completed(tasks):
        completed.append(await task)

    return completed

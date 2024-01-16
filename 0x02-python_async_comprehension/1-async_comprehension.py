#!/usr/bin/env python3
"""Async comprehension function"""
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Asynchronous coroutine that collects 10 random numbers
    using async comprehension over async_generator.
    return: List of 10 random numbers
    """
    return [k async for k in async_generator()]

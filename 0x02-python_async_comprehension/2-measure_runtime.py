#!/usr/bin/env python3
"""Run time for four parallel comprehensions.

Functions:
    measure_runtime()
"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Returns the total runtime of four parallel comprehensions."""

    start = time.perf_counter()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    total = time.perf_counter() - start

    return total

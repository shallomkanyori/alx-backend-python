#!/usr/bin/env python3
"""Measure the runtime

Functions:
    measure_time(n, max_delay)
"""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measures total execution time for wait_n.

    Args:
        n: The number of times to pass into wait_n.
        max_delay: The max_delay to pass in wait_n.

    Returns:
        float: The total execution time of wait_n(n, max_delay) / n.
    """

    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    total = time.perf_counter() - start

    return total / n

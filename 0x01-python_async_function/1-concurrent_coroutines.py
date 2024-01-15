#!/usr/bin/env python3
"""Multiple concurrent coroutines

Functions:
    wait_n(n, max_delay)
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawns wait_random n times with the specified max_delay.

    Args:
        n: The number of times to spawn wait_random.
        max_delay: The max_delay to spawn wait_random with.

    Returns:
        List of floats: The list of all the delays.
    """

    res = []

    for _ in range(n):
        wait_time = await wait_random(max_delay)
        res.append(wait_time)

    return res

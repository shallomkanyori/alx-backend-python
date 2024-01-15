#!/usr/bin/env python3
"""Tasks

Functions:
    task_wait_n(n, max_delay)
"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Spawns and executes task_wait_random n times with max_delay.

    Args:
        n: The number of times to spawn and execute task_wait_random.
        max_delay: The max_delay to spawn and execute task_wait_random with.

    Returns:
        List of floats: The list of all the delays.
    """

    res = []
    tasks = [task_wait_random(max_delay) for _ in range(n)]

    for task in asyncio.as_completed(tasks):
        wait_time = await task
        res.append(wait_time)

    return res

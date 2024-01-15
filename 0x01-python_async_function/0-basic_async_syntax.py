#!/usr/bin/env python3
"""Async Basics

Functions:
    wait_random(max_delay)
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Asynchronously waits for a random delay then returns the delay.

    Args:
        max_delay: The maximum delay. The function waits for a random delay
                   between 0 and max_delay.
    """

    wait_time = random.uniform(0, max_delay)
    await asyncio.sleep(wait_time)

    return wait_time

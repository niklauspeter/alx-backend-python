#!/usr/bin/env python3
"""asynchronous coroutine that takes in an integer argument
(max_delay, with a default value of 10) named wait_random that waits for a random delay between 0 and max_delay"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Returns a random float between 0 and max_delay
    Args:
        max_delay: The maximum delay to return
    Returns:
        A random float between 0 and max_delay
    """
    rand = random.uniform(0, max_delay)
    await asyncio.sleep(rand)
    return rand

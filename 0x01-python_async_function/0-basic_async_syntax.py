#!/usr/bin/env python3
"""
A module that delays a certain amount of time and returns it
"""

import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    """
    Args:
        max_delay (int, optional): the maximum delay. Defaults to 10.

    Returns:
        float: a random float between 0 and max_delay
    """
    rand = random.uniform(0, max_delay)
    await asyncio.sleep(rand)
    return rand

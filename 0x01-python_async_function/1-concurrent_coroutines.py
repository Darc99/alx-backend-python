#!/usr/bin/env python3
"""
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawns wait_random n times with a specified delay

    Args:
        n (int): number of times to spawn
        max_delay (int): max delay between each call

    Returns:
        List[float]: list of delays
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
    
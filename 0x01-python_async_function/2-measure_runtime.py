#!/usr/bin/env python3
"""
"""

from time import perf_counter
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n

def measure_time(n: int, max_delay: int) -> float:
    """_summary_

    Args:
        n (int): number of coroutines
        max_delay (int): max amount of time to wait for each coroutine

    Returns:
        float: elapsed time in secs
    """
    start = perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed = perf_counter() - start
    return elapsed/n

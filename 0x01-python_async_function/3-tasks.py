#!/usr/bin/env python3
"""
"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random

def task_wait_random(max_delay: int) -> asyncio.Task:
    """_summary_

    Args:
        max_delay (int): max number of secs that the task will wait

    Returns:
        asyncio.Task: _description_
    """
    return asyncio.create_task(wait_random(max_delay))

#!/usr/bin/env python3
"""A a method that returns a task"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """task that waits for a random number of seconds

    Args:
        max_delay (int): maximum number of seconds that the task will wait

    Returns:
        asyncio.Task: _description_
    """
    return asyncio.create_task(wait_random(max_delay))

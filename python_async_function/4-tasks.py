#!/usr/bin/env python3
"""
    Defines a function named task_wait_random that takes an integer max_delay
    and returns a asyncio.Task.
"""
import asyncio
from typing import List


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
        Creates a task for the wait_random coroutine.

        Args:
            max_delay (int): The maximum delay (in seconds) to wait.

        Returns:
            The list of all the delays (float values).
    """
    wait_random = __import__("0-basic_async_syntax").wait_random
    return asyncio.create_task(wait_random(max_delay))


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
        Takes in two int arguments (in this order): n and max_delay.

        Args:
            n (int): The number of times where wait_random is called.
            max_delay (int): The maximum delay (in seconds) to wait.

        Returns:
            The list of all the delays (float values).
    """
    list_of_delays = []
    task_in_progress = []

    for i in range(n):
        delay_created = task_wait_random(max_delay)
        task_in_progress.append(delay_created)

    for res in asyncio.as_completed(task_in_progress):
        delay = await res
        list_of_delays.append(delay)

    return list_of_delays

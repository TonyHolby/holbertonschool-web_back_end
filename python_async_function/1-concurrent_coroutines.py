#!/usr/bin/env python3
"""
    Defines an asynchronous routine named wait_n that takes in two
    integer arguments and returns a list of random delay with the
    wait_random function imported from 0-basic_async_syntax.py.
"""
import asyncio
from typing import List
wait_random = __import__("0-basic_async_syntax").wait_random



async def wait_n(n: int, max_delay: int) -> List[float]:
    """
        Takes in two int arguments (in this order): n and max_delay.

        Args:
            n (int): The number of times where wait_random is called.
            max_delay (int): The maximum delay (in seconds) to wait.

        Returns:
            wait_n should return the list of all the delays (float values).
    """
    list_of_delays = []
    task_in_progress = []

    for i in range(n):
        delay_created = asyncio.create_task(wait_random(max_delay))
        task_in_progress.append(delay_created)

    for res in asyncio.as_completed(task_in_progress):
        delay = await res
        list_of_delays.append(delay)

    return list_of_delays

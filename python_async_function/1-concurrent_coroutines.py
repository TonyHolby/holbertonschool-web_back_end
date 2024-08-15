#!/usr/bin/env python3
"""
    Defines an asynchronous routine named wait_n that takes in two
    integer arguments and returns a list of random delay with the
    wait_random function imported from 0-basic_async_syntax.py.
"""
import asyncio
from 0-basic_async_syntax import wait_random
from typing import List


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
    delay_stored = []

    for i in range(n):
        delay_created = asyncio.create_task(wait_random(max_delay))
        delay_stored.append(delay_created)

    for res in asyncio.as_completed(delay_stored):
        delay = await res
        list_of_delays.append(delay)

    return list_of_delays

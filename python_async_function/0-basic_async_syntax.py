#!/usr/bin/env python3
"""
    Defines an asynchronous coroutine named wait_random that takes in an
    integer argument and returns a random delay between 0 and max_delay
    seconds.
"""
import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    """
        Takes in an integer argument (max_delay, with a default value of 10).

        Args:
            max_delay (int): The maximum delay (in seconds) to wait.

        Returns:
            A random delay between 0 and max_delay (included and float value)
            seconds.
        """
    the_delay = random.uniform(0, max_delay)
    await asyncio.sleep(the_delay)
    return the_delay

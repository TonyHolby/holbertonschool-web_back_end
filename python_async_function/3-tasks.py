#!/usr/bin/env python3
"""
    Defines a function named task_wait_random that takes an integer max_delay
    and returns a asyncio.Task.
"""
import time
import asyncio
wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> float:
    """
        Takes an integer max_delay.

        Args:
            max_delay (int): The maximum delay (in seconds) to wait.

        Returns:
            A asyncio.Task.
    """
    asyncio.Task = asyncio.create_task(wait_random(max_delay))

    return asyncio.Task

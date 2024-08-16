#!/usr/bin/env python3
"""
    Defines a function named measure_time that measure the total
    time for wait_n(n, max_delay) imported from 1-concurrent_coroutines.py
    and returns the result of total_time / n (float value).
"""
import time
import asyncio
wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
        Measure the total execution time for wait_n.

        Args:
            n (int): The number of times where wait_random is called.
            max_delay (int): The maximum delay (in seconds) to wait.

        Returns:
            The result of total_time / n (float value).
    """
    start_measure = time.time()
    asyncio.run(wait_n(n, max_delay))
    finish_measure = time.time()

    total_time = finish_measure - start_measure

    return total_time / n

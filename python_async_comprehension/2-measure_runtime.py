#!/usr/bin/env python3
"""
    Defines a coroutine named measure_runtime that execute async_comprehension
    four times in parallel using asyncio.gather and returns the total runtime.
"""
import asyncio
import time
async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """
        Returns the runtime after the execution four times in parallel of
        async_comprehension.
    """
    start_measure_time = time.perf_counter()
    tasks = [async_comprehension() for i in range(4)]
    await asyncio.gather(*tasks)
    end_measure_time = time.perf_counter()

    return end_measure_time - start_measure_time

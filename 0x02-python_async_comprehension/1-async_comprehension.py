#!/usr/bin/env python3
""" Async Comprehension """
import asyncio
import typing

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> typing.List[float]:
    """
    collects and returns the 10 random numbers from the async generator
    """
    return [num
            async for num in async_generator()
            ]

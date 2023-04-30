#!/usr/bin/env python3
""" Asynchronous Generator """
import random
import asyncio
import typing


async def async_generator() -> typing.Generator[float,
                                                None,
                                                None]:
    """
    Async_generator - generates random number between
    0 and 10 using coroutine to loop 10 times each time
    asynchronously
    """
    for i in range(10):
        await asyncio.sleep(1)
        # yield returns value from the coroutime without termination
        yield random.uniform(0, 10)

# SuperFastPython.com
# example of calling run from within a coroutine
import asyncio


# example of defining another coroutine
async def another_custom():
    print("Another coroutine")


# custom coroutine
async def custom_coro(message):
    print(message)
    # create another coroutine
    another_coro = another_custom()
    # attempt to run the coroutine
    asyncio.run(another_coro)


# create and execute coroutine
asyncio.run(custom_coro("hello world"))

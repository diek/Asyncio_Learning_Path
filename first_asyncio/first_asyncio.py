import asyncio


# Define a coroutine
async def custom_routine():
    for idx, letter in enumerate("First Asyncio"):
        await asyncio.sleep(idx)
        print(letter)


# Run the coroutine only when executed directly
if __name__ == "__main__":
    asyncio.run(custom_routine())

import asyncio


# Define a coroutine
async def custom_routine(message):
    return f"Got: {message}"
    # for idx, letter in enumerate(message):
    #     await asyncio.sleep(idx)
    #     print(letter)


# Run the coroutine only when executed directly
if __name__ == "__main__":
    result = asyncio.run(custom_routine("1st Asyncio"))
    print(result)

import asyncio


async def greet():
    for i in range(3):
        await asyncio.sleep(1)
        print(f"Greeting {i+1}: Hello!")


async def farewell():
    for i in range(3):
        await asyncio.sleep(1.5)
        print(f"Farewell {i+1}: Goodbye!")


async def main():
    # Run both coroutines at the same time
    await asyncio.gather(greet(), farewell())


if __name__ == "__main__":
    asyncio.run(main())

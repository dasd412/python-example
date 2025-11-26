import asyncio


async def task1():
    print("Task 1 started")
    await asyncio.sleep(2)
    print("Task 1 ended")


async def task2():
    print("Task 2 started")
    await asyncio.sleep(2)
    print("Task 2 ended")


async def main():
    await asyncio.gather(task1(), task2())


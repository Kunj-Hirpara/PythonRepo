# Normal Synchronous Function
# import time

# def task(name):
#     print("Start: ", name)
#     time.sleep(2)
#     print("Ended: ", name)

# Sequential Execution
# task("Task 1")
# task("Task 2")


# Asynchronous Function
# Simple Asynchronous Function
# import asyncio

# async def hello():
#     print("Hello")
#     await asyncio.sleep(2)
#     print("World!")

# asyncio.run(hello())


# Multiple Asynchronous Functions
# import asyncio

# async def task(name):
#     print("Start: ", name)
#     await asyncio.sleep(2)
#     print("Ended: ", name)

# Concurrent Execution
# async def main():
#     await asyncio.gather(
#         task("Task 1"),
#         task("Task 2")
#     )

# asyncio.run(main())

# Multiple Asynchronous Functions
import asyncio

async def task(name, seconds):
    print("Start: ", name)
    await asyncio.sleep(seconds)
    print("Ended: ", name)

async def main():
    await asyncio.gather(
        task("Task 1", 2),
        task("Task 2", 3),
        task("Task 3", 1)
    )
asyncio.run(main())
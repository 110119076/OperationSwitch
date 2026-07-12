import asyncio
import time

async def fetch_data(delay):
    await asyncio.sleep(delay)
    return f"Result after {delay} seconds"

async def main():
    # Create tasks manually
    task1 = asyncio.create_task(fetch_data(1))
    task2 = asyncio.create_task(fetch_data(2))
    result1 = await task1
    result2 = await task2
    print(f"Task1 and Task2 awaited results: {[result1, result2]}")

    # Gather coroutines
    coroutines = [fetch_data(i) for i in range(1, 3)]
    results = await asyncio.gather(*coroutines, return_exceptions=True)
    print(f"Coroutines gathered results: {results}")

    # Gather tasks
    tasks = [asyncio.create_task(fetch_data(i)) for i in range(1, 3)]
    results = await asyncio.gather(*tasks, return_exceptions=True)
    print(f"Tasks gathered results: {results}")

    # Task Groups
    async with asyncio.TaskGroup() as tg:
        results = [tg.create_task(fetch_data(i)) for i in range(1, 3)]
        # All tasks are awaited automatically when the context manager exits
    print(f"TaskGroup results: {[task.result() for task in results]}")

    return "Main Coroutine Completed"

t1 = time.perf_counter()

results = asyncio.run(main())
print(results)

t2 = time.perf_counter()
print(f"Total time taken: {t2 - t1:.2f} seconds")

# Output:
# Task1 and Task2 awaited results: ['Result after 1 seconds', 'Result after 2 seconds']
# Coroutines gathered results: ['Result after 1 seconds', 'Result after 2 seconds']
# Tasks gathered results: ['Result after 1 seconds', 'Result after 2 seconds']
# TaskGroup results: ['Result after 1 seconds', 'Result after 2 seconds']
# Main Coroutine Completed
# Total time taken: 8.05 seconds

# It took 8 seconds because we are executing 4 sets of tasks sequentially, each taking 2 seconds 
# to complete. The first set of tasks is executed using manual task creation and awaiting, 
# the second set uses asyncio.gather() to gather coroutines, the third set uses asyncio.gather() to 
# gather tasks, and the fourth set uses asyncio.TaskGroup() to manage tasks. Each set of tasks is 
# executed sequentially, resulting in a total execution time of 8 seconds.
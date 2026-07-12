import asyncio
import time

async def fetch_data(delay):
    print(f"Delay value: {delay}")
    await asyncio.sleep(delay)
    print(f"Fetched data after {delay} seconds")
    return f"Result after {delay} seconds"

async def main():
    task1 = fetch_data(1)
    task2 = fetch_data(2)
    result1 = await task1
    print("Task1 fully completed")
    result2 = await task2
    print("Task2 fully completed")
    return [result1, result2]

t1 = time.perf_counter()

results = asyncio.run(main())
print(results)

t2 = time.perf_counter()
print(f"Total time taken: {t2 - t1:.2f} seconds")

# Output:
# Delay value: 1
# Fetched data after 1 seconds
# Task1 fully completed
# Delay value: 2
# Fetched data after 2 seconds
# Task2 fully completed
# ['Result after 1 seconds', 'Result after 2 seconds']
# Total time taken: 3.03 seconds

# This also took 3 seconds to complete both tasks because they were executed sequentially,
# blocking the main thread until each task was completed. However, the use of asyncio.create_task() 
# allows for concurrent execution of tasks, which can significantly reduce the total execution time.
import asyncio
import time

async def fetch_data(delay):
    print(f"Delay value: {delay}")
    await asyncio.sleep(delay)
    print(f"Fetched data after {delay} seconds")
    return f"Result after {delay} seconds"

async def main():
    task1 = asyncio.create_task(fetch_data(1))
    task2 = asyncio.create_task(fetch_data(2))
    result2 = await task2
    print("Task2 fully completed")
    result1 = await task1
    print("Task1 fully completed")
    return [result1, result2]

t1 = time.perf_counter()

results = asyncio.run(main())
print(results)

t2 = time.perf_counter()
print(f"Total time taken: {t2 - t1:.2f} seconds")

# Output:
# Delay value: 1
# Delay value: 2
# Fetched data after 1 seconds
# Fetched data after 2 seconds
# Task2 fully completed
# Task1 fully completed
# ['Result after 1 seconds', 'Result after 2 seconds']
# Total time taken: 2.02 seconds

# This took only 2 seconds to complete both tasks because they were executed concurrently,
# however, the order of completion was different from the previous example. Task2 completed first, 
# followed by Task1, demonstrating that the order of task completion can vary when tasks are 
# executed concurrently. Also await ensures that the main function waits for the completion of the 
# tasks before proceeding, and the results are returned in the order of the await statements, 
# not the order of task creation.
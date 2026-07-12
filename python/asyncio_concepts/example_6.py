import asyncio
import time
from concurrent.futures import ProcessPoolExecutor

def fetch_data(delay):
    print(f"Delay value: {delay}")
    time.sleep(delay)
    print(f"Fetched data after {delay} seconds")
    return f"Result after {delay} seconds"

async def main():
    # Run in threads
    task1 = asyncio.create_task(asyncio.to_thread(fetch_data, 1))
    task2 = asyncio.create_task(asyncio.to_thread(fetch_data, 2))
    result1 = await task1
    print("Thread1 fully completed")
    result2 = await task2
    print("Thread2 fully completed")

    # Run in process pool
    loop = asyncio.get_running_loop()

    with ProcessPoolExecutor() as executor:
        task1 = loop.run_in_executor(executor, fetch_data, 1)
        task2 = loop.run_in_executor(executor, fetch_data, 2)

        result1 = await task1
        print("Process1 fully completed")
        result2 = await task2
        print("Process2 fully completed")
    
    return [result1, result2]

if __name__ == "__main__":
    t1 = time.perf_counter()

    results = asyncio.run(main())
    print(results)

    t2 = time.perf_counter()
    print(f"Total time taken: {t2 - t1:.2f} seconds")

# Output:
# Delay value: 1
# Delay value: 2
# Fetched data after 1 seconds
# Thread1 fully completed
# Fetched data after 2 seconds
# Thread2 fully completed
# Delay value: 1
# Delay value: 2
# Fetched data after 1 seconds
# Process1 fully completed
# Fetched data after 2 seconds
# Process2 fully completed
# ['Result after 1 seconds', 'Result after 2 seconds']
# Total time taken: 4.47 seconds

# It took 4 seconds because we ran the tasks in threads and processes concurrently.
# We added __name__ == "__main__" to ensure that the code is only executed when the script 
# is run directly, and not when it is imported as a module. This is important for 
# multiprocessing to avoid issues with spawning new processes.

# The asyncio.to_thread() function is used to run the fetch_data function in a separate thread,
# while the loop.run_in_executor() method is used to run the fetch_data function in a separate 
# process using a ProcessPoolExecutor. By seperate thread we mean that the function is executed 
# in a different thread of the same process, while by separate process we mean that the function 
# is executed in a completely different process with its own memory space.
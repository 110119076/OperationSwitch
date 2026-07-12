import time

# All are synchronous functions, so they will block the main thread until they are completed.
def fetch_data(delay):
    print(f"Delay value: {delay}")
    time.sleep(delay)
    print(f"Fetched data after {delay} seconds")
    return f"Result after {delay} seconds"

def main():
    result1 = fetch_data(1)
    print("Fetch1 fully completed")
    result2 = fetch_data(2)
    print("Fetch2 fully completed")
    return [result1, result2]

t1 = time.perf_counter()

results = main()
print(results)
t2 = time.perf_counter()
print(f"Total time taken: {t2 - t1:.2f} seconds")

# Output:
# Delay value: 1
# Fetched data after 1 seconds
# Fetch1 fully completed
# Delay value: 2
# Fetched data after 2 seconds
# Fetch2 fully completed
# ['Result after 1 seconds', 'Result after 2 seconds']
# Total time taken: 3 seconds

# It took 3 seconds to complete both tasks because they were executed sequentially, 
# blocking the main thread until each task was completed.
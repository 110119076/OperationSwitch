import time
import threading
from concurrent.futures import ThreadPoolExecutor

# 1) Synchronous execution

# start = time.perf_counter()

# def do_something():
#     print("Sleeping 1 second...")
#     time.sleep(1)
#     print("Done sleeping...")

# do_something()

# finish = time.perf_counter()

# print(f"Finished in {round(finish-start, 2)} second(s)")

# Output:

# Sleeping 1 second...
# Done sleeping...
# Finished in 1.0 second(s)

# Because the function is executed synchronously, the program waits for the function to complete 
# before moving on to the next line of code. This results in a total execution time of 
# approximately 1 second.

# Asynchronous execution

# start = time.perf_counter()

# def do_something():
#     print("Sleeping 1 second...")
#     time.sleep(1)
#     print("Done sleeping...")

# t = threading.Thread(target=do_something)
# t.start()

# finish = time.perf_counter()

# print(f"Finished in {round(finish-start, 2)} second(s)")

# Output:

# Sleeping 1 second...
# Finished in 0.0 second(s)
# Done sleeping...

# Because the function is executed asynchronously in a separate thread, the program does not 
# wait for the function to complete before moving on to the next line of code. This results in a 
# total execution time of approximately 0 seconds, as the main thread continues executing while 
# the separate thread is sleeping.

# 3) Asynchronous execution with join() that holds the main thread until the separate thread completes.

# start = time.perf_counter()

# def do_something():
#     print("Sleeping 1 second...")
#     time.sleep(1)
#     print("Done sleeping...")

# t = threading.Thread(target=do_something)
# t.start()
# t.join()
# finish = time.perf_counter()

# print(f"Finished in {round(finish-start, 2)} second(s)")

# Output:

# Sleeping 1 second...
# Done sleeping...
# Finished in 1.0 second(s)

# Because the function is executed asynchronously in a separate thread, but the main thread waits 
# for the separate thread to complete using join(), the program does not move on to the next line 
# of code until the separate thread has finished executing. This results in a total execution time 
# of approximately 1 second, as the main thread is blocked until the separate thread completes.

# 4) Asynchronous execution with join() with multiple threads and args

# start = time.perf_counter()

# def do_something(delay):
#     print(f"Sleeping {delay} second...")
#     time.sleep(delay)
#     print("Done sleeping...")

# threads = []
# for _ in range(10):
#     t = threading.Thread(target=do_something, args=[1])
#     t.start()
#     threads.append(t)

# for t in threads:
#     t.join()

# finish = time.perf_counter()

# print(f"Finished in {round(finish-start, 2)} second(s)")

# Output:

# Sleeping 1 second...
# Sleeping 1 second...
# Sleeping 1 second...
# Sleeping 1 second...
# Sleeping 1 second...
# Sleeping 1 second...
# Sleeping 1 second...
# Sleeping 1 second...
# Sleeping 1 second...
# Sleeping 1 second...
# Done sleeping...
# Done sleeping...
# Done sleeping...
# Done sleeping...
# Done sleeping...
# Done sleeping...
# Done sleeping...
# Done sleeping...
# Done sleeping...
# Done sleeping...
# Finished in 1.0 second(s)

# If the same is executed synchronously, the total execution time would be approximately 10 seconds, 
# as each function call would block the main thread until it completes. However, by executing the 
# function asynchronously in separate threads, the program can continue executing while the 
# separate threads are sleeping, resulting in a total execution time of approximately 1 second.

# 5) Asynchronous execution with join() with multiple threads and args, but with ThreadPoolExecutor

# start = time.perf_counter()

# def do_something(delay):
#     print(f"Sleeping {delay} second...")
#     time.sleep(delay)
#     return f"Done sleeping...{delay}"

# delays = [5,4,3,2,1]

# with ThreadPoolExecutor() as executor:
#     results = executor.map(do_something, delays)

# finish = time.perf_counter()

# print(f"Finished in {round(finish-start, 2)} second(s)")

# Output:

# Sleeping 5 second...
# Sleeping 4 second...
# Sleeping 3 second...
# Sleeping 2 second...
# Sleeping 1 second...
# Finished in 5.0 second(s)

# The ThreadPoolExecutor allows for the concurrent execution of multiple threads, and the 
# executor.map() method allows for the mapping of a function to a list of arguments. In this case, 
# the do_something() function is mapped to a list of delays, resulting in the concurrent execution 
# of multiple threads that sleep for different amounts of time. The total execution time is 
# approximately equal to the longest delay, which is 5 seconds in this case.

# 6) Asynchronous execution with ThreadPoolExecutor but with results being returned and printed

start = time.perf_counter()

def do_something(delay):
    print(f"Sleeping {delay} second...")
    time.sleep(delay)
    return f"Done sleeping...{delay}"

delays = [5,4,3,2,1]

with ThreadPoolExecutor() as executor:
    results = executor.map(do_something, delays)
    
    for result in results:
        print(result)

finish = time.perf_counter()

print(f"Finished in {round(finish-start, 2)} second(s)")

# Output:

# Sleeping 5 second...
# Sleeping 4 second...
# Sleeping 3 second...
# Sleeping 2 second...
# Sleeping 1 second...
# Done sleeping...5
# Done sleeping...4
# Done sleeping...3
# Done sleeping...2
# Done sleeping...1
# Finished in 5.0 second(s)

# All the print(result) statements are executed after the corresponding do_something() function 
# has completed, and the results are returned in the order that the function calls were made. 
# The total execution time is still approximately equal to the longest delay, which is 5 seconds 
# in this case.
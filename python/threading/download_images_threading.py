import requests
import time
from concurrent.futures import ThreadPoolExecutor

img_urls = [
    'https://images.unsplash.com/photo-1516117172878-fd2c41f4a759',
    'https://images.unsplash.com/photo-1532009324734-20a7a5813719',
    'https://images.unsplash.com/photo-1524429656589-6633a470097c',
    'https://images.unsplash.com/photo-1530224264768-7ff8c1789d79',
    'https://images.unsplash.com/photo-1564135624576-c5c88640f235',
    'https://images.unsplash.com/photo-1541698444083-023c97d3f4b6',
    'https://images.unsplash.com/photo-1522364723953-452d3431c267',
    'https://images.unsplash.com/photo-1513938709626-033611b8cc03',
    'https://images.unsplash.com/photo-1507143550189-fed454f93097',
    'https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e',
    'https://images.unsplash.com/photo-1504198453319-5ce911bafcde',
    'https://images.unsplash.com/photo-1530122037265-a5f1f91d3b99',
    'https://images.unsplash.com/photo-1516972810927-80185027ca84',
    'https://images.unsplash.com/photo-1550439062-609e1531270e',
    'https://images.unsplash.com/photo-1549692520-acc6669e2f0c'
]

t1 = time.perf_counter()

def download_image(img_url):
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[3]
    with open(f"downloads/{img_name}", 'wb') as img_file:
        img_file.write(img_bytes)
        print(f"{img_name} was downloaded...")

with ThreadPoolExecutor() as executor:
    executor.map(download_image, img_urls)

t2 = time.perf_counter()
print(f"Finished in {t2-t1} seconds")

# Output:

# photo-1516117172878-fd2c41f4a759 was downloaded...
# photo-1504198453319-5ce911bafcde was downloaded...
# photo-1507143550189-fed454f93097 was downloaded...
# photo-1513938709626-033611b8cc03 was downloaded...
# photo-1532009324734-20a7a5813719 was downloaded...
# photo-1530224264768-7ff8c1789d79 was downloaded...
# photo-1541698444083-023c97d3f4b6 was downloaded...
# photo-1564135624576-c5c88640f235 was downloaded...
# photo-1550439062-609e1531270e was downloaded...
# photo-1516972810927-80185027ca84 was downloaded...
# photo-1522364723953-452d3431c267 was downloaded...
# photo-1524429656589-6633a470097c was downloaded...
# photo-1549692520-acc6669e2f0c was downloaded...
# photo-1530122037265-a5f1f91d3b99 was downloaded...
# photo-1493976040374-85c8e12f0c0e was downloaded...

# Finished in 5.088753899999574 seconds

# Asynchronous execution of the code using ThreadPoolExecutor results in a total execution time of 
# approximately 5.1 seconds, which is significantly faster than the synchronous execution time of 
# approximately 9.3 seconds. This demonstrates the benefits of concurrent execution when 
# downloading multiple images.

# This works because it is I/O bound, and the ThreadPoolExecutor allows for concurrent execution of 
# multiple threads, which can improve performance when dealing with I/O-bound tasks like 
# downloading images.

# But for CPU-bound tasks, using ThreadPoolExecutor may not provide significant performance 
# improvements, and in some cases, it may even result in slower execution times due to the overhead 
# of managing multiple threads. In such cases, using ProcessPoolExecutor or other parallel 
# processing techniques may be more appropriate.
from webscrapping.preprocessing import merge_excel_files
from webscrapping.multithreadwebscraping import threaded_function, multiple_threaded_function
from datetime import datetime
import time

start = time.perf_counter()

multiple_threaded_function(start=0, end=50, no_of_threads=4)

merge_excel_files()

finish = time.perf_counter()

print(f'{finish-start:0.5f} Seconds Time Taken for Processing at {str(datetime.now())}')

# 1. NCC -> Data Management
# 2. Summer Internship -> LinuxWorld
# 3. CoViD Internship -> Confirmation not sent yet
# 4. Project -> Streaming -> Kafka
# 5. Udacity Nanodegree -> Streaming Data
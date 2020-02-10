import time
from webscraping import Indeed
start = time.perf_counter()

Indeed.get_jobs(0, 10000)


finish = time.perf_counter()

print(f'{finish-start} Time Taken for processing')
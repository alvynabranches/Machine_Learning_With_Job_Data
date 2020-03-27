from webscrapping.webscraping import Indeed
from webscrapping.preprocessing import merge_excel_files
from locations import unique_locations
from __init__ import chrome_driver_location
from threaded import ThreadPooled, Threaded
from datetime import datetime
import time

start = time.perf_counter()

ThreadPooled.configure(max_workers=1024)

@Threaded(daemon=True)
def threaded_function(start, end, location):
    try:
        Indeed.get_jobs(start, end, webdriver_location=chrome_driver_location, location=location)
    except Exception as e:
        print(e)

def multiple_threaded_function(start, end, no_of_threads, location_list=unique_locations):
    load_on_single_thread = abs((end - start) // no_of_threads)
    for e in location_list:
        ts = []
        '''
        start -> starting page for the whole loop
        end -> ending page for the whole loop
        no_of_threads -> no of threads you what to start for the process
        NOTE: (end - start) / no_of_threads should be a positive integer
        '''
        for i in range(0, no_of_threads):
            ts.append(threaded_function(i*load_on_single_thread, (i+1)*load_on_single_thread, e))
            
        for t in ts:
            t.start()

        for t in ts:
            t.join()

multiple_threaded_function(start=0, end=100, no_of_threads=2)

merge_excel_files()

finish = time.perf_counter()

print(f'{finish-start} Seconds Time Taken for Processing at {str(datetime.now())}')
# 3911, 2780, 4213, 1783, 6187, 216, 21580, 103
# 1, 5, 4, 4, 2, [70], [47, 48, 49, 50], [13, 14, 15, 16, 17, 18, 19, 20
from threaded import ThreadPooled, Threaded
from __init__ import chrome_driver_location
from webscrapping.webscraping import Indeed

ThreadPooled.configure(max_workers=1024)

@Threaded(daemon=True)
def threaded_function(start, end, location, query=''):
    try:
        Indeed.get_jobs(start, end, webdriver_location=chrome_driver_location, location=location, query=query)
    except Exception as e:
        print(e)

def multiple_threaded_function(start, end, no_of_threads, location_list, job_list=['']):
    '''
        start -> starting page for the whole loop
        end -> ending page for the whole loop
        no_of_threads -> no of threads you what to start for the process
        NOTE: (end - start) / no_of_threads should be a positive integer
    '''
    load_on_single_thread = abs((end - start) // no_of_threads)
    _l = 0
    _t = 0
    for location in location_list:
        _l += 1
        print(f'{_l} / {len(location_list)} Locations Processing')
        _j = 0
        location = str(location)
        for job in job_list:
            _j += 1
            _t += 1
            if _j == 1:
                print(f'{_j} / {len(location_list)} Positions Processing')
            print(f'{_t} / {len(location_list) * len(job_list)} Processing')
            ts = []
            for i in range(0, no_of_threads):
                ts.append(threaded_function((i+start) * load_on_single_thread, (i+start+1) * load_on_single_thread, location, job))
                
            for t in ts:
                t.start()

            for t in ts:
                t.join()
from webscrapping.webscraping import Indeed
from webscrapping.preprocessing import merge_excel_files
from threaded import ThreadPooled, Threaded
import time

start = time.perf_counter()
# Indeed.get_jobs(0, 10, location='India')

# cities_in_Goa = ['Panjim', 'Mapuca', 'Porvorim', 'Calangute', 'Vagator', 'Bicholim', 'Navelim', 'Goa Velha', 'Pernem', 'Margao', 'Margaon+H+O', 'Verna', 'Verem', 'Thivim', '']

ThreadPooled.configure(max_workers=1024)

@Threaded(daemon=True)
def threaded_function(start, end, location):
    try:
        Indeed.get_jobs(start, end, location)
    except Exception as e:
        print(e)

def multiple_threaded_function(start, end, no_of_threads, location_list=['Bangalore', 'Pune']):
    load_on_single_thread = abs((end - start) // no_of_threads)
    for e in location_list:
        ts = []
        '''
        start -> starting page for the whole loop
        end -> ending page for the whole loop
        no_of_threads -> no of threads you what to start for the process
        NOTE: (end - start) / no_of_threads should be a positive integer
        '''
        for i in range(start, end):
            ts.append(threaded_function(i*load_on_single_thread, (i+1)*load_on_single_thread, e))
        # ts.append(merge_excel_files())
            
        for t in ts:
            t.start()

        for t in ts:
            t.join()

multiple_threaded_function(0, 100, 2)
merge_excel_files()

finish = time.perf_counter()

print(f'{finish-start} Seconds Time Taken for Processing')
# 3911, 2780, 4213, 1783, 6187, 216, 21580, 103
# 1, 5, 4, 4, 2, [70], [47, 48, 49, 50], [13, 14, 15, 16, 17, 18, 19, 20]
# 1. Utkarsh -> GUI
# 2. Mangirish -> NLP
# 3. Alvyn -> Preprocessing
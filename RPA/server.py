from webscraping import Indeed
from preprocessing import preprocess
from threaded import ThreadPooled, Threaded
import time

start = time.perf_counter()
# Indeed.get_jobs(0, 10, location='India')

# cities_in_Goa = ['Panjim', 'Mapuca', 'Porvorim', 'Calangute', 'Vagator', 'Bicholim', 'Navelim', 'Goa Velha', 'Pernem', 'Margao', 'Margaon+H+O', 'Verna', 'Verem', 'Thivim', '']

ThreadPooled.configure(max_workers=1024)

@Threaded(daemon=True)
def threaded_function(start, end):
    try:
        Indeed.get_jobs(start, end, location='Maharashtra')
    except Exception as e:
        print(e)
        break

def multiple_threaded_function(start, end, no_of_threads):
    load_on_single_thread = abs((end - start) // no_of_threads)
    ts = []
    '''
    start -> starting page for the whole loop
    end -> ending page for the whole loop
    no_of_threads -> no of threads you what to start for the process
    NOTE: (end - start) / no_of_threads should be a positive integer
    '''
    for i in range(0, no_of_threads):
        ts.append(threaded_function(i*load_on_single_thread, (i+1)*load_on_single_thread))
    ts.append(preprocess())
        
    for t in ts:
        t.start()

    for t in ts:
        t.join()

multiple_threaded_function(0, 500, 10)

finish = time.perf_counter()

print(f'{finish-start} Seconds Time Taken for Processing')
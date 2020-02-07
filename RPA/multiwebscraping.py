import multiprocessing as mp
import concurrent as cc

class MultiProcessWebScraping():

    @staticmethod
    def multiprocesses(target, no_of_processes, load_per_process):
        '''
        no_of_processes: No of processes that needs to be started
        load_per_process: No of load to be put on, on a single process
        '''

        processes = []
        for no in range(no_of_processes):
            processes.append(mp.Process(target=target, args=[no*load_per_process, (no+1)*load_per_process]))

        for process in processes:
            process.join()
    
    @staticmethod
    def multiprocessesconcurent(target):
        processes = []
        with cc.futures.ProcessPoolExecutor() as executor:
            processes.append(executor.submit(target, [0, 1]))
            processes[0].result()
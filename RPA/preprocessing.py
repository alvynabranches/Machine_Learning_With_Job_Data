from time import sleep, perf_counter
from threaded import ThreadPooled, Threaded
import os
import pandas as pd

ThreadPooled.configure(max_workers=1024)

@Threaded(daemon=True)
def preprocess():
    while(True):
        s = perf_counter()
        files = []
        df = pd.DataFrame()
        try:
            try:
                df = pd.read_excel('indeed_results_new.xlsx')
            except:
                df = pd.DataFrame()
            for n, file in enumerate(os.listdir('data/')):
                if file.endswith('.xlsx'):
                    print(f'{n+1}, {file}')
                    df = df.append(pd.read_excel('data/'+file), ignore_index=True)
                    files.append('data/'+file)
                print(f"{pd.read_excel('indeed_results_new.xlsx').shape[0]} Items Found So Far")
            df.drop_duplicates().to_excel('indeed_results_new.xlsx', index=False)
            for file in files:
                os.remove(file)
        except Exception as e:
            print(e)
        e = perf_counter()
        print(f"{round(e-s, 2)} Seconds Time Taken to Process")
        sleep(5)
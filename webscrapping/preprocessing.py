from time import sleep, perf_counter
import os
import pandas as pd
from datetime import datetime

from __init__ import download_directory, project_directory

def merge_excel_files():
    s = perf_counter()
    files = []
    if os.path.isfile(project_directory + 'indeed_results.xlsx'):
        df = pd.read_excel(project_directory + 'indeed_results.xlsx')
    else:
        df = pd.DataFrame(columns=['Title','Location', 'Company', 'Salary', 'Sponsored', 'Description', 'Time'])
    try:
        for n, file in enumerate(os.listdir(download_directory)):
            if file.endswith('.xlsx') or file.endswith('.XLSX'):
                print(f'{n+1}, {file}')
                df = df.append(pd.read_excel(download_directory+file), ignore_index=True)
                files.append(download_directory+file)
        df.drop_duplicates().to_excel(project_directory + 'indeed_results.xlsx', index=False)
        for file in files:
            os.remove(file)
    except Exception as e:
        print(e)
    e = perf_counter()
    print(f"{pd.read_excel(project_directory + 'indeed_results.xlsx').shape[0]} Items Found So Far at {datetime.now()}")
    print(f"{round(e-s, 2)} Seconds Were Taken to Merge")
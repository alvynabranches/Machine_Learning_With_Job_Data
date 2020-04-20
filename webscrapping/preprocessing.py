from time import sleep, perf_counter
import os
import pandas as pd
from datetime import datetime
from preprocessing.preprocess_data import apply_preprocessing_on_fields

from __init__ import download_directory, webscrapping_directory

def merge_excel_files():
    s = perf_counter()
    files = []
    if os.path.isfile(webscrapping_directory+'indeed_results_new.xlsx'):
        df = pd.read_excel(webscrapping_directory+'indeed_results_new.xlsx')
    else:
        df = pd.DataFrame(columns=['Title','Location', 'Company', 'Salary', 'Sponsored', 'Description', 'Time'])
    try:
        for n, file in enumerate(os.listdir(download_directory)):
            if file.endswith('.xlsx') or file.endswith('.XLSX'):
                print(f'{n+1}, {file}')
                df = df.append(pd.read_excel(download_directory+file), ignore_index=True)
                files.append(download_directory+file)
        df.drop_duplicates().to_excel(webscrapping_directory+'indeed_results_new.xlsx', index=False)
        for file in files:
            os.remove(file)
    except Exception as e:
        print(e)
    e = perf_counter()
    print(f"{pd.read_excel(webscrapping_directory+'indeed_results_new.xlsx').shape[0]} Items Found So Far at {datetime.now()}")
    print(f"{round(e-s, 2)} Seconds Time Taken to Process")
    sleep(5)
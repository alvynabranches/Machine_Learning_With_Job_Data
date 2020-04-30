from webscrapping.preprocessing import merge_excel_files
from webscrapping.multithreadwebscraping import multiple_threaded_function
from ml.preprocessing.preprocess_data import apply_preprocessing_on_fields
from locations import unique_locations, unique_pincodes
from jobs import unique_jobs
from datetime import datetime, date, timedelta
from time import perf_counter
import pandas as pd
import os
from __init__ import project_directory, non_preprocessed_dataset, spark_mongo_server_connection_string
from ml.website.app import app as mlapp
from bigdata.website.app import app as bigdataapp
from threaded import ThreadPooled, Threaded
# from pyspark import SparkContext, SparkConf

# sc = SparkContext(conf=SparkConf().set("spark.jars.packages", "org.mongodb.spark:mongo-spark-connector_2.11:2.3.2"))
# sc.setLogLevel('WARN')

ThreadPooled.configure(max_workers=1024)

start = perf_counter()

# multiple_threaded_function(start=0, end=3, no_of_threads=3, location_list=unique_locations, job_list=unique_jobs)

# merge_excel_files()

# df = pd.read_excel(non_preprocessed_dataset)

# df = apply_preprocessing_on_fields(df)

# df.to_excel(f'indeed_results_pp_{str(date.today())}.xlsx', index=False)

finish = perf_counter()

# if __name__ == '__main__':
@Threaded('mlapp', False, True)
def startmlapp():
    mlapp.run_server()

@Threaded('bigdataapp', False, True)
def startbigdataapp():
    bigdataapp.run_server()

startmlapp().start()
startbigdataapp().start()

print(f'{finish-start:0.5f} Seconds Time Taken for Processing at {str(datetime.now())}')
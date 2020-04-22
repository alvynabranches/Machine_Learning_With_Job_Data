from webscrapping.preprocessing import merge_excel_files
from webscrapping.multithreadwebscraping import multiple_threaded_function
from ml.preprocessing.preprocess_data import apply_preprocessing_on_fields
from locations import unique_locations, unique_pincodes
from jobs import unique_jobs
from datetime import datetime
from time import perf_counter
import pandas as pd
from pyspark import SparkContext, SparkConf

sc = SparkContext(conf=SparkConf().set("spark.jars.packages", "org.mongodb.spark:mongo-spark-connector_2.11:2.3.2"))
sc.setLogLevel('WARN')

start = perf_counter()

multiple_threaded_function(start=0, end=2, no_of_threads=1, location_list=['Pune', 'Chennai'], job_list=unique_jobs)

merge_excel_files()

df = pd.read_excel('./indeed_results.xlsx')

df = apply_preprocessing_on_fields(df)

df.to_excel(f'indeed_results_pp_{str(datetime.now())}.xlsx')

finish = perf_counter()

print(f'{finish-start:0.5f} Seconds Time Taken for Processing at {str(datetime.now())}')
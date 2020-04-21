from webscrapping.preprocessing import merge_excel_files
from webscrapping.multithreadwebscraping import multiple_threaded_function
from locations import unique_locations, unique_pincodes
from jobs import unique_jobs
from datetime import datetime
from time import perf_counter
from pyspark import SparkContext, SparkConf

sc = SparkContext(conf=SparkConf().set("spark.jars.packages", "org.mongodb.spark:mongo-spark-connector_2.11:2.3.2"))
sc.setLogLevel('WARN')

start = perf_counter()

multiple_threaded_function(start=0, end=10, no_of_threads=2,location_list=['Mumbai', 'Pune'], job_list=['Data+Scientist', 'Data Analyst'])
# , job_list=unique_jobs

merge_excel_files()

finish = perf_counter()

print(f'{finish-start:0.5f} Seconds Time Taken for Processing at {str(datetime.now())}')
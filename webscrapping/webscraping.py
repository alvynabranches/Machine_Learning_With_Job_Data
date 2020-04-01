from bs4 import BeautifulSoup
from datetime import date
from datetime import datetime
from datetime import timedelta
from selenium import webdriver
from time import perf_counter

import hashlib
import pandas as pd
import os

from __init__ import download_directory

df = pd.DataFrame(columns=['Title','Location','Company','Salary','Sponsored','Description','Time'])

class Indeed():
    
    @staticmethod
    def get_jobs(start, end, webdriver_location, location='Pune', query=''):
        '''
            start: The starting page of search to retrieve data from
            end: The ending page of search to retrieve data from
            location: which particular place, city or country you want to retrive data of
            
            This is a static method hence will return the dataframe which is processed during the training
        '''
        
        df = pd.DataFrame(columns=['Title','Location','Company','Salary','Sponsored','Description','Time'])
        driver = webdriver.Chrome(webdriver_location)

        title = None
        loc = None
        company = None
        salary = None
        sponsored = None
        time = None
        job_desc = None
        _s = 0
        driver.maximize_window()
        for i in range(start, end):
            _s += 1
            print(f'{_s} / {end-start} Jobs Processing')
            try:
                driver.get('https://www.indeed.co.in/jobs?q='+ query +'&l='+location+'&start='+str(i))
                
                for job in driver.find_elements_by_class_name('result'):
                    soup = BeautifulSoup(job.get_attribute('innerHTML'),'html.parser')

                    try:
                        title = soup.find('a',class_='jobtitle').text.replace('\n','').strip()
                    except:
                        title = None

                    try:
                        loc = soup.find(class_='location').text
                    except:
                        loc = None

                    try:
                        company = soup.find(class_='company').text.replace('\n','').strip()
                    except:
                        company = None

                    try:
                        salary = soup.find(class_='salary').text.replace('\n','').strip()
                    except:
                        salary = None
                    
                    try:
                        sponsored = soup.find(class_='sponsoredGray').text
                        sponsored = 'Sponsored'
                    except:
                        sponsored = 'Organic'

                    sum_div = job.find_element_by_xpath('./div[3]')

                    try:
                        sum_div.click()
                    except:
                        close_button = driver.find_elements_by_class_name('popover-x-button-close')[0]
                        close_button.click()
                        sum_div.click()

                    try:
                        _time = soup.find(class_='date').text
                        if _time == 'Just posted' or _time == 'Today':
                            time = str(date.today())
                        elif _time == '1 day ago':
                            time = str(date.today() - timedelta(days=1))
                        elif _time == '2 days ago':
                            time = str(date.today() - timedelta(days=2))
                        elif _time == '3 days ago':
                            time = str(date.today() - timedelta(days=3))
                        elif _time == '4 days ago':
                            time = str(date.today() - timedelta(days=4))
                        elif _time == '5 days ago':
                            time = str(date.today() - timedelta(days=5))
                        elif _time == '6 days ago':
                            time = str(date.today() - timedelta(days=6))
                        elif _time == '7 days ago':
                            time = str(date.today() - timedelta(days=7))
                        elif _time == '8 days ago':
                            time = str(date.today() - timedelta(days=8))
                        elif _time == '9 days ago':
                            time = str(date.today() - timedelta(days=9))
                        elif _time == '10 days ago':
                            time = str(date.today() - timedelta(days=10))
                        elif _time == '11 days ago':
                            time = str(date.today() - timedelta(days=11))
                        elif _time == '12 days ago':
                            time = str(date.today() - timedelta(days=12))
                        elif _time == '13 days ago':
                            time = str(date.today() - timedelta(days=13))
                        elif _time == '14 days ago':
                            time = str(date.today() - timedelta(days=14))
                        elif _time == '15 days ago':
                            time = str(date.today() - timedelta(days=15))
                        elif _time == '16 days ago':
                            time = str(date.today() - timedelta(days=16))
                        elif _time == '17 days ago':
                            time = str(date.today() - timedelta(days=17))
                        elif _time == '18 days ago':
                            time = str(date.today() - timedelta(days=18))
                        elif _time == '19 days ago':
                            time = str(date.today() - timedelta(days=19))
                        elif _time == '20 days ago':
                            time = str(date.today() - timedelta(days=20))
                        elif _time == '21 days ago':
                            time = str(date.today() - timedelta(days=21))
                        elif _time == '22 days ago':
                            time = str(date.today() - timedelta(days=22))
                        elif _time == '23 days ago':
                            time = str(date.today() - timedelta(days=23))
                        elif _time == '24 days ago':
                            time = str(date.today() - timedelta(days=24))
                        elif _time == '25 days ago':
                            time = str(date.today() - timedelta(days=25))
                        elif _time == '26 days ago':
                            time = str(date.today() - timedelta(days=26))
                        elif _time == '27 days ago':
                            time = str(date.today() - timedelta(days=27))
                        elif _time == '28 days ago':
                            time = str(date.today() - timedelta(days=28))
                        elif _time == '29 days ago':
                            time = str(date.today() - timedelta(days=29))
                        elif _time == '30 days ago':
                            time = str(date.today() - timedelta(days=30))
                        else:
                            time = None
                    except:
                        time = None

                    try:
                        job_desc = driver.find_element_by_id('vjs-desc').text
                    except:
                        job_desc = None
                    df = df.append({'Title':title,'Location':location,'Company':company,'Salary':salary,'Sponsored':sponsored,'Description':job_desc, 'Time':time},ignore_index=True)
                    
            except Exception as e:
                print(e)

            finally:
                try:
                    if not os.path.isdir(download_directory):
                        os.mkdir(download_directory)
                    n = download_directory + str(hashlib.md5(str(datetime.now()).encode()).hexdigest().encode()).replace("b'", '').replace("'", '') + '.xlsx'
                    df.to_excel(n, index=False)
                except Exception as e:
                    print(e)
        driver.close()
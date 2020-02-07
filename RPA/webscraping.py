from selenium import webdriver
import pandas as pd 
from bs4 import BeautifulSoup
import hashlib
import datetime
import multiprocessing as mp
import concurrent as cc

df = pd.DataFrame(columns=['Title','Location','Company','Salary','Sponsored','Description','Time'])
class Indeed():
    
    @staticmethod
    def get_data(start, end, location='India', webdriver_location='D:/A/3T_Project/chromedriver.exe'):
        '''
        start: The starting page of search to retrieve data from
        end: The ending page of search to retrieve data from
        location: which particular place, city or country you want to retrive data of
        
        This is a static method hence will return the dataframe which is processed during the training
        '''
        df = pd.DataFrame(columns=['Title','Location','Company','Salary','Sponsored','Description','Time'])
        driver = webdriver.Chrome(webdriver_location)

        for i in range(start, end):
            driver.get('https://www.indeed.co.in/jobs?q=&l='+location+'&start='+str(i))
            driver.implicitly_wait(4)

            for job in driver.find_elements_by_class_name('result'):

                soup = BeautifulSoup(job.get_attribute('innerHTML'),'html.parser')

                try:
                    title = soup.find('a',class_='jobtitle').text.replace('\n','').strip()
                except:
                    title = None

                try:
                    location = soup.find(class_='location').text
                except:
                    location = None

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
                    time = soup.find(class_='date').text
                except:
                    time = None

                try:
                    job_desc = driver.find_element_by_id('vjs-desc').text
                except:
                    job_desc = None
                finally:
                    pass

                df = df.append({'Title':title,'Location':location,'Company':company,'Salary':salary,'Sponsored':sponsored,'Description':job_desc, 'Time':time},ignore_index=True)
        
        n = str(datetime.datetime.now()).encode()
        n = hashlib.sha512(n).hexdigest().encode()
        n = str(n).replace("'", '') + '.xlsx'
        df.to_excel(n)
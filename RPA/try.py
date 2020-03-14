import pandas as pd
import numpy as np

import time
from datetime import date
from datetime import timedelta

import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ChromeOptions
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException

import os, zipfile
import shutil
import glob

class RPA:
    def dates_between(self, start_date, end_date):
        date = start_date
        days = (end_date - start_date).days + 1
        dates = []
        def return_dd_mm_yyyy_date_format(date):
            dd = ''
            mm = ''
            yyyy = ''
            if date.day < 10:
                dd = '0' + str(date.day)
            else:
                dd = str(date.day)
            if date.month < 10:
                mm = '0' + str(date.month)
            else:
                mm = str(date.month)
            yyyy = date.year
            return {'date':dd, 'month':mm, 'year':yyyy}
        for _ in range(days):
            dates.append(return_dd_mm_yyyy_date_format(date))
            date += timedelta(days=1)
        return dates
    
    def download(self):
        start_date, end_date = date(2019, 1, 1), date(2019, 1, 31)
        try:
            chromeOptions = webdriver.ChromeOptions()
            chromeOptions.add_experimental_option("prefs", {"download.default_directory": r"D:\Downloads","download.prompt_for_download": False,"download.directory_upgrade": True,"safebrowsing.enabled": True})

            driverLoc = "D:/A/3T_Project/chromedriver.exe"
            browser = webdriver.Chrome(driverLoc, chrome_options=chromeOptions)
            browser.maximize_window()
            browser.get('https://www.bseindia.com/markets/MarketInfo/BhavCopy.aspx')
            browser.implicitly_wait(5)
            browser.find_elements_by_xpath('/html/head/iframe')

            browser.implicitly_wait(3)
            for e in self.dates_between(start_date, end_date):
                day, month, year = e['date'], e['month'], e['year']

                sel_day = Select(browser.find_element_by_xpath('//*[@id="ContentPlaceHolder1_fdate1"]'))

                sel_day.select_by_value(day)

                browser.implicitly_wait(2)

                sel_month = Select(browser.find_element_by_xpath('//*[@id="ContentPlaceHolder1_fmonth1"]'))
                sel_month.select_by_value(month)

                sel_year = browser.find_element_by_xpath('//*[@id="ContentPlaceHolder1_fyear1"]')
                sel_year.send_keys(year)
                
                submit_btn = browser.find_element_by_xpath('//*[@id="ContentPlaceHolder1_btnSubmit"]')
                submit_btn.click()

                browser.implicitly_wait(3)
                try:
                    on_date = browser.find_element_by_xpath('//*[@id="ContentPlaceHolder1_btnHylSearBhav"]')
                    on_date.click()
                except:
                    pass
                browser.implicitly_wait(3)
        except:
            os._exit(1)         

            
    def unzip(self):
        des = r'D:/stock/data/'
        extension = ".zip"
        y = os.listdir(des)
        print("Got data")
        os.chdir(des)
        for item in os.listdir(des):
            if item.endswith(item):
                file_name = os.path.abspath(item)
                zip_ref = zipfile.ZipFile(file_name)
                zip_ref.extractall(des)
                zip_ref.close()
                os.remove(file_name)
                print("Zipping Done")

    def addcolumn(self):
        try:
            des='D:/Downloads/'
            newdes='D:/Downloads/'
            print("Got data")
            os.chdir(des)
            for file in os.listdir(des):
                if file.endswith(file):
                    df = pd.read_csv(file, encoding='utf-8')
                    df['filename'] = str(file.split('.')[0][2:])
                    os.listdir(des).append(df)
                    print(df['filename'][0])
                    df.to_csv(newdes+file)
        except:
            pass

    def merging(self):
        os.chdir(r'D:\Downloads')
        extension = 'CSV'
        all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
        combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
        combined_csv.to_csv(r'D:\Downloads\merged.csv', index=False, encoding='utf-8-sig')

r = RPA()
r.download()
r.unzip()
r.addcolumn()
r.merging()
#browser.close()
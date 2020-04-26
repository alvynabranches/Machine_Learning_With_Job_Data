import pandas as pd
from numpy.random import randint
from datetime import date
from datetime import timedelta
from warnings import filterwarnings
from ml.preprocessing.cleansing import preprocessing_description, preprocessing_title, preprocessing_company
from ml.preprocessing.cleansing import preprocessing_location, preprocessing_salary, salary_remove_unit, get_skills
from ml.preprocessing.cleansing import get_salary_average, get_experience_senior, get_experience_junior, transform_title
from ml.preprocessing.cleansing import unique_skills
def apply_preprocessing_on_fields(df):
    filterwarnings('ignore')
    '''
        NOTE: df should be a pandas DataFrame
    '''
    # df = df[(df['Title'].notnull()) & (df['Description'].notnull()) & (df['Salary'].notnull())]
    df['Title'] = df['Title'].apply(lambda x: preprocessing_title(x))
    df['Location'] = df['Location'].apply(lambda x: preprocessing_location(x))
    df['Company'] = df['Company'].apply(lambda x: preprocessing_company(x))
    df['Description'] = df['Description'].apply(lambda x: preprocessing_description(x))
    df['Description'] = df['Description'].apply(lambda x: ('' if x == 'nan' else x))
    df['Salary'] = df['Salary'].apply(lambda x: preprocessing_salary(x))
    df['Salary'] = df['Salary'].apply(lambda x: '' if x == 'nan' else x)
    df['Time'] = df['Time'].apply(lambda x: str(date.today() - timedelta(days=randint(31, 181))) if str(x) == 'nan' else x)

    df['Salary_Unit_Month'] = 0
    df['Salary_Unit_Year'] = 0
    df['Salary_Unit_Week'] = 0
    df['Salary_Unit_Day'] = 0
    df['Salary_Unit_Hour'] = 0
    for i in range(df.shape[0]):
        if df['Salary'][i].endswith('month'):
            df['Salary_Unit_Month'][i] = 1
        elif df['Salary'][i].endswith('year'):
            df['Salary_Unit_Year'][i] = 1
        elif df['Salary'][i].endswith('week'):
            df['Salary_Unit_Week'][i] = 1
        elif df['Salary'][i].endswith('day'):
            df['Salary_Unit_Day'][i] = 1
        elif df['Salary'][i].endswith('hour'):
            df['Salary_Unit_Hour'][i] = 1
    
    df['Salary_New'] = df['Salary'].apply(lambda x: salary_remove_unit(x))
    df['Salary_Average'] = df['Salary_New'].apply(lambda x: get_salary_average(x))

    _year = 12         # 12 months in a year
    _month = 1         # retain the month value as it is
    _week = 4          # 4 weeks in a month
    _day  = 6 * _week   # 6 working days a week, 4 weeks in a month
    _hour = 8 * _day    # 8 hours a day, 6 working days a week, 4 weeks in a month
    df['Monthly_Salary'] = 0
    for i in range(df.shape[0]):
        if df['Salary_Unit_Year'][i] == 1:
            df['Monthly_Salary'][i] = df['Salary_Average'][i] / _year
        elif df['Salary_Unit_Month'][i] == 1:
            df['Monthly_Salary'][i] = df['Salary_Average'][i] * _month
        elif df['Salary_Unit_Week'][i] == 1:
            df['Monthly_Salary'][i] = df['Salary_Average'][i] * _week
        elif df['Salary_Unit_Day'][i] == 1:
            df['Monthly_Salary'][i] = df['Salary_Average'][i] * _day
        elif df['Salary_Unit_Hour'][i] == 1:
            df['Monthly_Salary'][i] = df['Salary_Average'][i] * _hour

    df['Job_Type_Part_Time'] = 0
    df['Job_Type_Full_Time'] = 0
    for i in range(df.shape[0]):
        if df['Description'][i].find('part time') != -1:
            df['Job_Type_Part_Time'][i] = 1
        if df['Description'][i].find('full time') != -1:
            df['Job_Type_Full_Time'][i] = 1

    df['XP_Experience'] = 0
    df['XP_Fresher'] = 0

    for i in range(df.shape[0]):
        if df['Description'][i].find('experienced') != -1 or df['Title'][i].find('experienced') != -1:
            df['XP_Experience'][i] = 1
        if df['Description'][i].find('fresher') != -1 or df['Title'][i].find('fresher') != -1:
            df['XP_Fresher'][i] = 1
        
    df['Gender'] = 0
    df['Gender_Male'] = 0
    df['Gender_Female'] = 0
    for i in range(df.shape[0]):
        if df['Description'][i].find(' male') != -1:
            df['Gender_Male'][i] = 1
        if df['Description'][i].find('female') != -1:
            df['Gender_Female'][i] = 1
        if df['Description'][i].find('female') != -1 and not df['Description'][i].find(' male') != -1:
            df['Gender'][i] = 0
        elif df['Description'][i].find(' male') != -1 and not df['Description'][i].find('female') != -1:
            df['Gender'][i] = 1
        else:
            df['Gender'][i] = 2

    df['Education_Tenth'] = 0
    df['Education_Twelvth'] = 0
    df['Education_Bachelors'] = 0
    df['Education_Masters'] = 0
    df['Education_Doctorate'] = 0
    for i in range(df.shape[0]):
        if df['Description'][i].find(' 10 ') != -1 or df['Description'][i].find('10th') != -1:
            df['Education_Tenth'][i] = 1
        if df['Description'][i].find(' 12 ') != -1 or df['Description'][i].find('12th') != -1 or df['Description'][i].find('higher secondary') != -1:
            df['Education_Twelvth'][i] = 1
        if df['Description'][i].find('bachelor degree') != -1 or df['Description'][i].find('bachelor s') != -1 or df['Description'][i].find(' ug ') != -1:
            df['Education_Bachelors'][i] = 1
        if df['Description'][i].find('masters degree') != -1 or df['Description'][i].find(' pg ') != -1:
            df['Education_Masters'][i] = 1
        if df['Description'][i].find('doctoral') != -1 or df['Description'][i].find('doctorate') != -1:
            df['Education_Doctorate'][i] = 1
        if df['Description'][i].find('ug or pg') != -1:
            df['Education_Bachelors'][i] = 1
            df['Education_Masters'][i] = 1
        
    df['Skills_Description'] = df['Description'].apply(lambda x: get_skills(x))
    df['Skills_Title'] = df['Title'].apply(lambda x: get_skills(x))
    df['Skills'] = df['Skills_Description'] + df['Skills_Title']
    df['Skills'] = df['Skills'].apply(lambda x: x[1:])
    df['Skills'] = df['Skills'].apply(lambda x: unique_skills(x))

    df['Position_Junior'] = df['Title'].apply(lambda x: get_experience_junior(x))
    df['Position_Senior'] = df['Title'].apply(lambda x: get_experience_senior(x))

    df['Internship'] = 0
    for i in range(df.shape[0]):
        if df['Description'][i].find('internship') != -1 or df['Description'][i].find('intern') != -1:
            df['Internship'][i] = 1
        if df['Title'][i].find('internship') != -1 or df['Title'][i].find('intern') != -1:
            df['Internship'][i] = 1

    df['Title_New'] = df['Title'].apply(lambda x: transform_title(x))

    df = df[df['Location'] != 'India'].reset_index().drop(['index'], axis=1)
    # df = df[df['Title'].notnull() & df['Description'].notnull() & df['Salary'].notnull()]
    
    return df
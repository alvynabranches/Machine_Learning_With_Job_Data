import pandas as pd
from warnings import filterwarnings
from webscrapping.cleansing import preprocessing_description, preprocessing_title_location_company, preprocessing_salary, salary_remove_unit
filterwarnings('ignore')

def apply_preprocessing_on_fields(df):
    '''
        NOTE: df should be a pandas DataFrame
    '''
    df['Title'] = df['Title'].apply(lambda x: preprocessing_title_location_company(x))
    df['Location'] = df['Location'].apply(lambda x: preprocessing_title_location_company(x))
    df['Company'] = df['Company'].apply(lambda x: preprocessing_title_location_company(x))
    df['Description'] = df['Description'].apply(lambda x: preprocessing_description(x))
    df['Salary'] = df['Salary'].apply(lambda x: preprocessing_salary(x))

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
    
    df['Salary_Average'] = 0
    for i in range(len(df['Salary_New'])):
        if len(df['Salary_New'][i].split()) == 2:
            df['Salary_Average'][i] = int((int(df['Salary_New'][i].split()[0]) + int(df['Salary_New'][i].split()[1]))/2)
        else:
            df['Salary_Average'][i] = df['Salary_New'][i]
    
    df = df[df['Location'] != 'India'].reset_index().drop(['index'], axis=1)

    return df
version = '0.0.23'
chrome_version = '80'

project_directory = './'

chrome_driver_location = project_directory + 'chromedriver/'+ chrome_version +'/chromedriver.exe'

webscrapping_directory =  project_directory + 'webscrapping/'
download_directory = webscrapping_directory + 'data/'

PreProcessing_Done = False
Machine_Learning_Done = False
GUI_Done = False

Libraries_Required = [
    'threaded',
    'selenium'
]
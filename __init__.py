version = '0.0.86'
chrome_version = '81'

project_directory = './'

chrome_driver_location = project_directory + 'chromedriver/'+ chrome_version +'/chromedriver'

webscrapping_directory =  project_directory + 'webscrapping/'
download_directory = webscrapping_directory + 'data/'

ip_address_and_port_no = '127.0.0.1'
db_name = 'jobDB'
col_name = 'webscrappingdata'

PreProcessing_Done = False
Machine_Learning_Done = False
GUI_Done = False

Libraries_Required = [
    'threaded',
    'selenium',

]
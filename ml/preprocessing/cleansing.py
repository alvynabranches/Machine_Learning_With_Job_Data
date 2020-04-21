def preprocessing_description(text):
    text = str(text).lower()

    for _ in range(100):
        text = text.replace('\n', ' ')

    for _ in range(10):
        text = text.replace('&', ' and ')
        text = text.replace('·', ' ')
        text = text.replace('/', ' ')
        text = text.replace('(', ' ')
        text = text.replace(')', ' ')
        text = text.replace('[', ' ')
        text = text.replace(']', ' ')
        text = text.replace(':', ' ')
        text = text.replace('.', ' ')
        text = text.replace('-', ' ')
        text = text.replace('#', ' ')
        text = text.replace("'", ' ')
        text = text.replace('"', ' ')
        text = text.replace('`', ' ')
        text = text.replace('|', ' ')
        text = text.replace(';', ' ')
        text = text.replace('<', ' ')
        text = text.replace('>', ' ')
        text = text.replace('?', ' ')
        text = text.replace('~', ' ')
        text = text.replace('!', ' ')
        text = text.replace('$', ' ')
        text = text.replace('%', ' ')
        text = text.replace('^', ' ')
        text = text.replace('*', ' ')
        text = text.replace('_', ' ')
        text = text.replace('+', ' ')
        text = text.replace('=', ' ')
        text = text.replace('{', ' ')
        text = text.replace('}', ' ')
        text = text.replace('–', ' ')
        text = text.replace('’', ' ')
        text = text.replace(',', '')

    for _ in range(3):
        text = text.replace(r'\uf0b7', ' ')
        text = text.replace('\uf0b7', ' ')
        text = text.replace('job summary ', ' ')
        text = text.replace('job description ', ' ')
        text = text.replace('salary ', ' ')
        text = text.replace('rs ', ' ')
        text = text.replace('\\', ' ')
    
    for _ in range(50):
        text = text.replace('  ', ' ')
    
    text = text.lstrip().rstrip()
    return text

def preprocessing_company(text):
    text = str(text)
    for _ in range(10):
        text = text.replace('&', 'and')
        text = text.replace("'", ' ')
        text = text.replace('"', ' ')
        text = text.replace('(', ' ')
        text = text.replace(')', ' ')
        text = text.replace('[', ' ')
        text = text.replace(']', ' ')
        text = text.replace('{', ' ')
        text = text.replace('}', ' ')
        text = text.replace('-', ' ')
        text = text.replace('#', ' ')
        text = text.replace('/', ' ')
        text = text.replace('!', ' ')
        text = text.replace('$', ' ')
        text = text.replace('%', ' ')
        text = text.replace('^', ' ')
        text = text.replace('*', ' ')
        text = text.replace('_', ' ')
        text = text.replace('+', ' ')
        text = text.replace('=', ' ')
        text = text.replace('<', ' ')
        text = text.replace('>', ' ')
        text = text.replace('?', ' ')
        text = text.replace('~', ' ')
        text = text.replace('`', ' ')
        text = text.replace('|', ' ')
        text = text.replace(';', ' ')
        text = text.replace('.', ' ')
        text = text.replace(',', ' ')
        text = text.replace(':', ' ')
        text = text.replace('\\', ' ')
        
    for _ in range(10):
        text = text.replace("  ", ' ')
    text = text.lstrip().rstrip()
    return text

def preprocessing_title(text):
    text = str(text)
    for _ in range(10):
        text = text.replace('&', 'and')
        text = text.replace("'", ' ')
        text = text.replace('"', ' ')
        text = text.replace('(', ' ')
        text = text.replace(')', ' ')
        text = text.replace('[', ' ')
        text = text.replace(']', ' ')
        text = text.replace('{', ' ')
        text = text.replace('}', ' ')
        text = text.replace('-', ' ')
        text = text.replace('#', ' ')
        text = text.replace('/', ' ')
        text = text.replace('!', ' ')
        text = text.replace('$', ' ')
        text = text.replace('%', ' ')
        text = text.replace('^', ' ')
        text = text.replace('*', ' ')
        text = text.replace('_', ' ')
        text = text.replace('+', ' ')
        text = text.replace('=', ' ')
        text = text.replace('<', ' ')
        text = text.replace('>', ' ')
        text = text.replace('?', ' ')
        text = text.replace('~', ' ')
        text = text.replace('`', ' ')
        text = text.replace('|', ' ')
        text = text.replace(';', ' ')
        text = text.replace('.', ' ')
        text = text.replace(',', ' ')
        text = text.replace(':', ' ')
        text = text.replace('\\', ' ')
        
    for _ in range(10):
        text = text.replace("  ", ' ')
    text = text.lstrip().rstrip().lower()
    return text

def preprocessing_location(text):
    text = str(text)
    for _ in range(10):
        text = text.replace('&', 'and')
        text = text.replace("'", ' ')
        text = text.replace('"', ' ')
        text = text.replace('(', ' ')
        text = text.replace(')', ' ')
        text = text.replace('[', ' ')
        text = text.replace(']', ' ')
        text = text.replace('{', ' ')
        text = text.replace('}', ' ')
        text = text.replace('-', ' ')
        text = text.replace('#', ' ')
        text = text.replace('/', ' ')
        text = text.replace('!', ' ')
        text = text.replace('$', ' ')
        text = text.replace('%', ' ')
        text = text.replace('^', ' ')
        text = text.replace('*', ' ')
        text = text.replace('_', ' ')
        text = text.replace('+', ' ')
        text = text.replace('=', ' ')
        text = text.replace('<', ' ')
        text = text.replace('>', ' ')
        text = text.replace('?', ' ')
        text = text.replace('~', ' ')
        text = text.replace('`', ' ')
        text = text.replace('|', ' ')
        text = text.replace(';', ' ')
        text = text.replace('.', ' ')
        text = text.replace(',', ' ')
        text = text.replace(':', ' ')
        text = text.replace('\\', ' ')

    for _ in range(10):
        text = text.replace("  ", ' ')
    text = text.lstrip().rstrip()
    return text

def preprocessing_salary(text):
    text = str(text)
    for _ in range(20):
        text = text.replace('&', ' and ')
        text = text.replace(',', '')
        text = text.replace('/', ' ')
        text = text.replace("'", ' ')
        text = text.replace('"', ' ')
        text = text.replace(':', ' ')
        text = text.replace('–', ' ')
        text = text.replace('.', ' ')
        text = text.replace('|', ' ')
        text = text.replace(';', ' ')
        text = text.replace('’', ' ')
        text = text.replace('?', ' ')
        text = text.replace('~', ' ')
        text = text.replace('!', ' ')
        text = text.replace('$', ' ')
        text = text.replace('%', ' ')
        text = text.replace('^', ' ')
        text = text.replace('*', ' ')
        text = text.replace('_', ' ')
        text = text.replace('+', ' ')
        text = text.replace('=', ' ')
        text = text.replace('`', ' ')
        text = text.replace('\\', ' ')
        text = text.replace('(', ' ')
        text = text.replace(')', ' ')
        text = text.replace('<', ' ')
        text = text.replace('>', ' ')
        text = text.replace('[', ' ')
        text = text.replace(']', ' ')
        text = text.replace('{', ' ')
        text = text.replace('}', ' ')
        
    for _ in range(5):
        text = text.replace('₹', '')
        text = text.replace('-', '')
        text = text.replace(' a ', ' ')
        text = text.replace(' an ', ' ')
    
    for _ in range(10):
        text = text.replace('  ', ' ')
    text = text.lstrip().rstrip().lower()
    return text

def salary_remove_unit(text):
    text = str(text)
    text = text.replace(' month', '')
    text = text.replace(' year', '')
    text = text.replace(' week', '')
    text = text.replace(' day', '')
    text = text.replace(' hour', '')

    text = text.lstrip().rstrip()
    return text

def get_skills(text):
    text = str(text)
    skills = ''
    if text.find('python') != -1:
        skills += '|python'
    if text.find('big') != -1 and text.find('data') != -1:
        skills += '|big data'
    if text.find('hadoop') != -1:
        skills += '|hadoop'
    if text.find('spark') != -1:
        skills += '|spark'
    if text.find('pyspark') != -1:
        skills += '|pyspark'
    if text.find('tableau') != -1:
        skills += '|tableau'
    if text.find('tensorflow') != -1:
        skills += '|tensorflow'
    if text.find('pytorch') != -1:
        skills += '|pytorch'
    if text.find('django') != -1:
        skills += '|django'
    if text.find('react') != -1 and text.find('js') != -1:
        skills += '|react.js'
    if text.find('angular js') != -1 or text.find('angularjs') != -1:
        skills += '|angular.js'
    if text.find('node js') != -1 or text.find('nodejs') != -1:
        skills += '|nodejs'
    if text.find('react native') != -1:
        skills += '|react native'
    if text.find('flume') != -1:
        skills += '|flume'
    if text.find('hive') != -1:
        skills += '|hive'
    if text.find('pig') != -1:
        skills += '|pig'
    if text.find('sql') != -1:
        skills += '|sql'
    if text.find('java') != -1:
        skills += '|java'
    if text.find('kotlin') != -1:
        skills += '|kotlin'
    if text.find('mongodb') != -1:
        skills += '|mongo'
    if text.find('statistics') != -1:
        skills += '|statistics'
    if text.find('mathamatics') != -1 or text.find('maths') != -1:
        skills += '|maths'
    if text.find(' r ') != -1:
        skills += '|r'
    if text.find('powerbi') != -1:
        skills += '|powerbi'
    if (text.find('excel') != -1 and text.find('microsoft')) or text.find('msexcel') != -1:
        skills += '|msexcel'
    if text.find('word') != -1 and (text.find('ms') != -1 or text.find('microsoft') != -1):
        skills += '|msword'
    if text.find('powerpoint') != -1 or text.find('mspowerpoint') != -1:
        skills += '|mspp'
    if text.find('soft') != -1 and text.find('skills'):
        skills += '|soft skills'
    if text.find('oracle db') != -1:
        skills += '|oracle db'
    if text.find('mysql') != -1:
        skills += '|mysql'
    if text.find('nosql') != -1:
        skills += '|nosql'
    if text.find(' ui ') != -1:
        skills += '|ui'
    if text.find(' ux ') != -1:
        skills += '|ux'
    if text.find('deep learning') != -1:
        skills += '|deep learning'
    if text.find('machine learning') != -1:
        skills += '|machine learning'
    if text.find(' c ') != -1:
        skills += '|c'
    if text.find('c++') != -1:
        skills += '|c++'
    if text.find('c#') != -1:
        skills += '|c#'
    if text.find('ubuntu') != -1:
        skills += '|ubuntu'
    if text.find('cent os') != -1:
        skills += '|centos'
    if text.find('centos') != -1:
        skills += '|centos'
    if text.find('php') != -1:
        skills += '|php'
    if text.find('javascript') != -1 or text.find(' js ') != -1:
        skills += '|javascript'
    if text.find('vue js') != -1:
        skills += '|vue js'
    if text.find('ml5 js') != -1:
        skills += '|ml5 js'
    if text.find('postgress') != -1:
        skills += '|postgress'
    if text.find('perl') != -1:
        skills += '|perl'
    if text.find('ruby') != -1:
        skills += '|ruby'
    if text.find('project management') != -1:
        skills += '|project management'
    if text.find(' html ') != -1:
        skills += '|html'
    if text.find(' css ') != -1:
        skills += '|css'
    if text.find('aws') != -1:
        skills += '|aws'
    if text.find('amazon web services') != -1:
        skills += '|aws'
    if text.find('cyber security') != -1:
        skills += '|cyber security'
    if text.find('fortran') != -1:
        skills += '|fortran'
    if text.find('julia') != -1:
        skills += '|julia'
    if text.find('cloud computing') != -1:
        skills += '|cloud computing'
    if text.find('google cloud platform') != -1 or text.find('gcp') != -1:
        skills += '|gcp'
    if text.find('blockchain') != -1:
        skills += '|blockchain'
    if text.find('front end') != -1:
        skills += '|front end'
    if text.find(' ai ') != -1 or text.find('artificial intelligence') != -1:
        skills += '|ai'
    if text.find('linux') != -1:
        skills += '|linux'
    return skills
def preprocessing_description(text):
    '''
        This function is used to remove the special characters and the unrequired text from description column
    '''
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
    '''
        This function is used to remove the special characters and the unrequired text from company column
    '''
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
    '''
        This function is used to remove the special characters and the unrequired text from location column
    '''
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
    '''
        This function is used to remove the special characters and the unrequired text from salary column
    '''
    text = str(text)
    for _ in range(20):
        text = text.replace('&', ' and ')
        text = text.replace(',', '')
        text = text.replace('/', ' ')
        text = text.replace("'", ' ')
        text = text.replace('"', ' ')
        text = text.replace(':', ' ')
        text = text.replace('–', ' ')
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
    '''
        This function is used to remove the salary unit from the salary field.
        NOTE: This function should only be used after removing the special characters and the extra spaces from it.
    '''
    text = str(text)
    text = text.replace(' month', '')
    text = text.replace(' year', '')
    text = text.replace(' week', '')
    text = text.replace(' day', '')
    text = text.replace(' hour', '')

    text = text.lstrip().rstrip()
    return text

def get_salary_average(text):
    text = str(text)
    if text != '':
        if len(text.split()) == 2:
            return int((float(text.split()[0]) + float(text.split()[1]))/2)
        else:
            return int(text)
    else:
        return 0

def get_experience_junior(text):
    if text.find(' jr') != -1 or text.find('jr ') != -1 or text.find('junior') != -1:
        return 1
    else:
        return 0

def get_experience_senior(text):
    if text.find('senior') != -1 or text.find('sr ') != -1 or text.find(' sr') != -1:
        return 1
    else:
        return 0

def get_skills(text):
    '''
        This function is used to get the skills from the description and title column. 
        NOTE: This function should only be used after removing the special characters and the extra spaces from it.
    '''
    text = str(text)
    skills = ''
    if text.find('python') != -1:
        skills += '|python'
    if text.find('big data') != -1 or text.find('bigdata') != -1:
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
    if (text.find('react') != -1 and text.find('js') != -1) or (text.find('react') != -1 and text.find('javascript') != -1):
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
    if text.find(' sql') != -1 or text.find('sql ') != -1:
        skills += '|sql'
    if text.find('java') != -1 and not text.find('java ee') != -1 and not text.find('java se') != -1 and not text.find('java me') != -1:
        skills += '|java'
    if text.find('java ee') != -1:
        skills += '|java ee'
    if text.find('java se') != -1:
        skills += '|java se'
    if text.find('java me') != -1:
        skills += '|java me'
    if text.find('kotlin') != -1:
        skills += '|kotlin'
    if text.find('mongodb') != -1 or text.find('mongo') != -1:
        skills += '|mongodb'
    if text.find('statistics') != -1:
        skills += '|statistics'
    if text.find('mathamatics') != -1 or text.find('maths') != -1:
        skills += '|maths'
    if text.find(' r ') != -1:
        skills += '|r'
    if text.find('powerbi') != -1:
        skills += '|powerbi'
    if (text.find('excel') != -1 and (text.find('microsoft') != -1 or text.find('ms') != -1)) or text.find('msexcel') != -1:
        skills += '|msexcel'
    if (text.find('word') != -1 and (text.find('ms') != -1 or text.find('microsoft') != -1)) or text.find('msword') != -1:
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
    if text.find('machine learning') != -1 or text.find(' ml ') != -1 or text.find(' ml') != -1 or text.find('ml ') != -1:
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
        skills += '|cloud'
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
    if text.find('software') != -1 and text.find('devol') != -1:
        skills += '|software devlopment'
    if text.find('redis') != -1:
        skills += '|redis'
    if text.find('redux') != -1:
        skills += '|redux'
    if text.find('groovy') != -1:
        skills += '|groovy'
    if text.find('elasticsearch') != -1:
        skills += '|elasticsearch'
    if text.find('cassandra') != -1:
        skills += '|cassandra'
    if text.find('bash') != -1:
        skills += '|bash'
    if text.find('unix') != -1:
        skills += '|unix'
    if text.find('ms sql') != -1 or text.find('ms database') != -1:
        skills += '|ms sql server'
    if text.find('agile') != -1:
        skills += '|agile'
    if text.find('jira') != -1:
        skills += '|jira'
    if text.find('workfront') != -1:
        skills += '|workfront'
    if text.find('scrum') != -1:
        skills += '|scrum'
    if text.find('kanban') != -1:
        skills += '|kanban'
    if text.find('cloud services') != -1:
        skills += '|cloud'
    if text.find('vb script net') != -1:
        skills += '|vb script net'
    if text.find(' net') != -1 or text.find('dotnet') != -1 or text.find('dot net') != -1:
        skills += '|.net'
    if text.find('microservices') != -1:
        skills += '|microservices'
    if text.find('unix') != -1:
        skills += '|unix'
    if text.find('redhat') != -1:
        skills += '|redhat'
    if text.find('linux') != -1:
        skills += '|linux'
    if text.find('data mining') != -1:
        skills += '|data mining'
    if text.find('data visual') != -1:
        skills += '|data visualization'
    if text.find('unstructured data') != -1:
        skills += '|unstructured data'
    if text.find('communication skills') != -1:
        skills += '|communication skills'
    if text.find('laravel') != -1:
        skills += '|laravel'
    if text.find('flask') != -1:
        skills += '|flask'
    if text.find('flutter') != -1:
        skills += '|flutter'
    if text.find('macos') != -1 or text.find('mac os') != -1:
        skills += '|macos'
    if text.find('windows os') != -1 or text.find('windowsos') != -1 or text.find('windows oper') != -1:
        skills += '|windows'
    if text.find('microcontroller') != -1:
        skills += '|microcontroller'
    if text.find('mern') != -1:
        skills += '|mern'
    if text.find('mean') != -1:
        skills += '|mean'
    if text.find('mevn') != -1:
        skills += '|mevn'
    if text.find('ios') != -1:
        skills += '|ios'
    if text.find('jquery') != -1:
        skills += '|jquery'
    if text.find('wamp') != -1:
        skills += '|wamp'
    if text.find('lamp') != -1:
        skills += '|lamp'
    if text.find('xampp') != -1:
        skills += '|xampp'
    if text.find('restapi') != -1 or text.find(' rest ') != -1 or text.find('restful api') != -1:
        skills += '|restapi'
    if text.find('bigquery') != -1 or text.find('big query') != -1:
        skills += '|bigquery'
    if text.find('windows server') != -1:
        skills += '|windows server'
    if text.find('sdlc') != -1:
        skills += '|sdlc'
    if text.find('mvp') != -1:
        skills += '|mvp'
    if text.find('mvc') != -1:
        skills += '|mvc'
    if text.find('objective c') != -1:
        skills += '|objective c'
    if text.find('git') != -1:
        skills += '|git'
    if text.find('junit') != -1:
        skills += '|junit'
    if text.find('jest') != -1:
        skills += '|jest'
    if text.find('mocha') != -1:
        skills += '|mocha'
    if text.find('enzyme') != -1:
        skills += '|enzyme'
    if text.find('android sdk') != -1:
        skills += '|android sdk'
    if text.find('mvvm') != -1:
        skills += '|mvvm'
    if text.find('iot') != -1:
        skills += '|iot'
    if text.find('gcm') != -1 or text.find('google cloud mes') != -1:
        skills += '|gcm'
    if text.find('wordpress') != -1:
        skills += '|wordpress'
    if text.find('codeigniter') != -1:
        skills += '|codeigniter'
    if text.find('joomla') != -1:
        skills += '|joomla'
    if text.find('content management system') != -1:
        skills += '|cms'
    if text.find('microsoft bi') != -1 or text.find('microsoft power bi') != -1 or text.find('powerbi') != -1:
        skills += '|microsoft bi'
    if text.find('asp net') != -1:
        skills += '|asp.net'
    if text.find('version control system') != -1 or text.find('vcs') != -1:
        skills += '|vcs'
    if text.find('tomcat') != -1:
        skills += '|apache tomcat'
    if text.find('plsql') != -1:
        skills += '|plsql'
    if text.find('tsql') != -1:
        skills += '|tsql'
    if text.find('bootstrap') != -1:
        skills += '|bootstrap'
    if text.find('opencv') != -1 or text.find('open cv') != -1:
        skills += '|opencv'
    if text.find('nerual network') != -1:
        skills += '|nn'
    if text.find('dreamweaver') != -1:
        skills += '|dreamweaver'
    if text.find('analytical skill') != -1:
        skills += '|analytics'
    if text.find('debugging skill') != -1:
        skills += '|debugging'
    if text.find('hibernate') != -1:
        skills += '|hibernate'
    if text.find('etl') != -1:
        skills += '|etl'
    if text.find('maven') != -1:
        skills += '|maven'
    if text.find('eclipse') != -1:
        skills += '|eclipse'
    if text.find('jboss') != -1:
        skills += '|jboss'
    if text.find('oops') != -1:
        skills += '|oops'
    if text.find('gateway') != -1:
        skills += '|gateway'
    if text.find('golang') != -1:
        skills += '|golang'
    if text.find('stripe') != -1:
        skills += '|stripe'
    if text.find('braintree') != -1:
        skills += '|braintree'
    if text.find('cloudfront') != -1:
        skills += '|cloudfront'
    if text.find('cloudwatch') != -1:
        skills += '|cloudwatch'
    if text.find('npm') != -1:
        skills += '|npm'
    if text.find('ajax') != -1:
        skills += '|ajax'
    if text.find('unit testing') != -1:
        skills += '|unit testing'
    if text.find('xml') != -1:
        skills += '|xml'
    if text.find('docker') != -1:
        skills += '|docker'
    if text.find('springboot') != -1  or text.find('spring boot') != -1:
        skills += '|springboot'
    if text.find('kubernetes') != -1:
        skills += '|kubernetes'
    if text.find('selenium') != -1:
        skills += '|selenium'
    if text.find('swift') != -1:
        skills += '|swift'
    if text.find('sqlite') != -1:
        skills += '|sqlite'
    if text.find('photoshop') != -1:
        skills += '|photoshop'
    return skills

def unique_skills(text):
    text = str(text)
    text = list(set(text.split('|')))
    text = '|'.join(text)
    return text

def transform_title(text):
    text = str(text)
    if text.find('data sci') != -1:
        return 'data scientist'
    elif text.find('web dev') != -1 or text.find('webdev') != -1:
        return 'web developer'
    elif text.find('graphic designer') != -1 or text.find('graphics designer') != -1:
        return 'graphic designer'
    elif text.find('system admin') != -1 or text.find('system administrator') != -1:
        return 'system admin'
    elif text.find('web graphic designer') != -1 or text.find('html 5 dev') != -1 or text.find('web design') != -1 or text.find('web front end developers') != -1 or text.find('front end dev') != -1 or text.find('react dev') != -1 or text.find('react js dev') != -1 or text.find('reactjs dev') != -1 or text.find('vue dev') != -1 or text.find('vue js dev') != -1 or text.find('vuejs dev') != -1 or text.find('angular js dev') != -1 or text.find('angularjs dev') != -1 or text.find('angular dev') != -1:
        return 'front end developer'
    elif text.find('ui ux') != -1:
        return 'ui ux developer'
    elif text.find('ui des') != -1 or text.find('ui dev') != -1:
        return 'ui developer'
    elif text.find('ux des') != -1 or text.find('ux dev') != -1:
        return 'ux developer'
    elif text.find('aws architect') != -1:
        return 'aws developer'
    elif text.find('full stack dev') != -1 or text.find('php full stack') != -1 or text.find('fullstack dev') != -1 or text.find('mean stack') != -1 or text.find('mern stack') != -1 or text.find('mevn stack') != -1 or text.find('mern dev') != -1 or text.find('mean dev') != -1 or text.find('mevn dev') != -1:
        return 'full stack developer'
    elif text.find('devops enigneer') != -1:
        return 'devops engineer'
    elif text.find('machine learning engineer') != -1 or text.find('machine learning program') != -1 or text.find('ml engineer') != -1 or text.find('ml dev') != -1:
        return 'machine learning developer'
    elif text.find('software eng') != -1 or text.find('dotnet dev') != -1 or text.find('software archi') != -1 or text.find('software dev') != -1 or text.find('net dev') != -1:
        return 'software developer'
    elif text.find('nodejs dev') != -1 or text.find('php dev') != -1:
        return 'back end developer'
    elif text.find('big data engineer') != -1 or text.find('hadoop engineer') != -1 or text.find('spark engineer') != -1:
        return 'big data engineer'
    elif text.find('data engineer') != -1 and not text.find('big data') != -1:
        return 'data engineer'
    elif text.find('android dev') != -1 or text.find('android app dev') != -1 or text.find('ios app dev') != -1 or text.find('ios dev') != -1:
        return 'mobile app developer'
    elif text.find('embedded eng') != -1:
        return 'embedded engineer'
    else:
        return None
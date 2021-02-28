from configparser import ConfigParser

config = ConfigParser()

config['API'] = {
    'user_uri': 'https://reqres.in',
    'book_uri': 'http://216.10.245.166',
    'github_uri': 'https://github.com'
}

config['MYSQLDB'] = {
    'user': 'root',
    'password': 'root',
    'host': 'localhost',
    'database': 'PythonAutomation'
}

config['FILES'] = {
    'use_cdn': 'false',
    'images_path': '/my_app/images'
}

with open('./configs/dev.ini', 'w') as f:
    config.write(f)

with open('./configs/properties.ini', 'w') as f:
    config.write(f)

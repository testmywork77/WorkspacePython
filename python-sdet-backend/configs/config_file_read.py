from configparser import ConfigParser

parser = ConfigParser()
parser.read('dev.ini')
print(parser.sections())  # ['api', 'settings', 'db', 'files']
print(parser.get('api', 'base_uri'))  # abc123
print(parser.get('api', 'book_uri'))  # abc123
print(parser.options('settings'))  # ['debug', 'secret_key', 'log_path']
print(parser['api']['base_uri'])
print(parser['api']['book_uri'])
print('db' in parser)  # True

parser = ConfigParser()
parser.read('properties.ini')
print(parser.sections())  # ['api', 'settings', 'db', 'files']
print(parser.get('api', 'base_uri'))  # abc123
print(parser.get('api', 'book_uri'))  # abc123
print(parser.options('settings'))  # ['debug', 'secret_key', 'log_path']
print(parser['api']['base_uri'])
print(parser['api']['book_uri'])
print('db' in parser)  # True



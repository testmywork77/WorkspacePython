from configparser import ConfigParser

parser = ConfigParser()
parser.read('dev.ini')

print(parser.sections())  # ['api', 'settings', 'db', 'files']
print(parser.get('settings', 'secret_key'))  # abc123
print(parser.options('settings'))  # ['debug', 'secret_key', 'log_path']
print(parser['api']['base_url'])
print('db' in parser)  # True



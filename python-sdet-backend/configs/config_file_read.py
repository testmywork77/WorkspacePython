from configparser import ConfigParser

parser = ConfigParser()
parser.read('./configs/dev.ini')
print(parser.sections())  # ['MYSQLDB', 'API', 'FILES']
print(parser.get('API', 'base_uri'))
print(parser.get('API', 'book_uri'))
print(parser.options('API'))
print('API' in parser)

parser = ConfigParser()
parser.read('./configs/properties.ini')
print(parser.sections())  # ['MYSQLDB', 'API', 'FILES']
print(parser.get('MYSQLDB', 'user'))
print(parser.get('MYSQLDB', 'password'))
print(parser.options('MYSQLDB'))
print('MYSQLDB' in parser)
import configparser


config = configparser.ConfigParser()
config.read('properties.ini')
print(config.sections())

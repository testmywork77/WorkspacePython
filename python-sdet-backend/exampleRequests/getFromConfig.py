import os
from configparser import ConfigParser
from utilities.configurations import *

# config = ConfigParser()
# config.read(r'..\utilities\properties.ini')
# config.read('../utilities/properties.ini')#

config = getConfig()
print(config['api']['book_uri'])
print(config
      ['api']['base_uri'])

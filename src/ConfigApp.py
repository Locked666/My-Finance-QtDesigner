import os 
import configparser

__version__= '1.0.0.0'

MODE_DEBUG = True
SALT_CRYPT = '06919904179'

## arquivo ini ###

config = configparser.ConfigParser()

config.read('config.ini')

PATH_DATABASE = config['Database']['database']


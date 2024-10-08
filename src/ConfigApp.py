import os 
import configparser

__version__= '1.0.0.0'

MODE_DEBUG = True


## arquivo ini ###

config = configparser.ConfigParser()

config.read('config.ini')

PATH_DATABASE = config['Database']['database']


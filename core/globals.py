# globals.py
# By: Adam Kraft

"""
A place for a few global variables to hang out
"""

# import libraries
import platform
import os

def initialize():
    global DIR_DELIM
    DIR_DELIM = '/' if platform.system() != 'Windows' else '\\'

    global DEV_MODE
    DEV_MODE = platform.system() != 'Windows'

    global BASE_DIR
    BASE_DIR = os.getcwd()

    global GAMES_CONFIG
    GAMES_CONFIG = BASE_DIR + DIR_DELIM + 'var' + DIR_DELIM + 'games_config.json'

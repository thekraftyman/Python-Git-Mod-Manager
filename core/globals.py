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

    global BASE_DIR
    DEV_MODE = platform.system() != 'Windows'

    global BASE_DIR
    BASE_DIR = os.getcwd()

    global CORE_GAME_FILES
    CORE_GAME_FILES = BASE_DIR + DIR_DELIM + 'var' + DIR_DELIM + 'core_files.json'

    global USER_VARS
    USER_VARS = BASE_DIR + DIR_DELIM + 'var' + DIR_DELIM + 'user_vars.json'

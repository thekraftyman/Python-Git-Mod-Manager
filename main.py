# main.py
# By: Adam Kraft

# import libraries
import platform # for testing on a non-windows device
import os
from core.misc import *
from shutil import copyfile, rmtree

# Fun Globals ---------
DIR_DELIM = '/' if platform.system() != 'Windows' else '\\'
BASE_DIR = os.getcwd()
CORE_GAME_FILES = BASE_DIR + DIR_DELIM + 'var' + DIR_DELIM + 'core_files.json'
USER_VARS = BASE_DIR + DIR_DELIM + 'var' + DIR_DELIM + 'user_vars.json'

def main():
    # initialize with user vars
    if not os.path.exists(USER_VARS):
        user_vars = {}
        user_vars['base_game_path'] = input('Paste full path to base Among Us directory: ')
        while not os.path.isdir(user_vars['base_game_path']):
            print(user_vars['base_game_path'])
            user_vars['base_game_path'] = input('Incorrect path given, please input full path: ')
        # write to json
        save_json(USER_VARS, user_vars)
    else:
        user_vars = load_json(USER_VARS)

    # get core files
    game_files = load_json(CORE_GAME_FILES)

    # create mods folder if none exists
    if not os.path.isdir('mods'):
        os.mkdir('mods')

    # get a list of mods
    mod_names = next(os.walk('mods'))[1]

    # create clean temporary game folder
    if os.path.isdir('among_us_game_tmp'):
        rmtree('among_us_game_tmp')
    os.mkdir('among_us_game_tmp')

    # copy core game files into tmp dir
    # ...

    # select mod from list
    # ...

    # copy mod from list into tmp folder
    # ...

    # run the game






if __name__=='__main__':
    main()

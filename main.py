# main.py
# By: Adam Kraft

# import libraries
import platform # for testing on a non-windows device
import os
from core.misc import *
from shutil import copyfile, rmtree

# Fun Globals ---------
DIR_DELIM = '/' if platform.system() != 'Windows' else '\\'
CORE_GAME_FILES = 'var' + DIR_DELIM + 'core_files.json'

def main():
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

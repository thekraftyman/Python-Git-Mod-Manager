# main.py
# By: Adam Kraft

# import libraries
import platform # for testing on a non-windows device
import os
from core.misc import *
from shutil import copyfile, rmtree, copytree

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
    tmp_game_dir = BASE_DIR + DIR_DELIM + 'among_us_game_tmp' + DIR_DELIM

    # copy core game files into tmp dir
    for filename in game_files['base_game_files']:
        if user_vars['base_game_path'].endswith('\\'):
            full_source = user_vars['base_game_path'] + filename
        else:
            full_source = user_vars['base_game_path'] + DIR_DELIM + filename

        full_dest = tmp_game_dir + filename
        copyfile(full_source,full_dest)

    # copy core game dirs
    for dirname in game_files['base_game_dirs']:
        if user_vars['base_game_path'].endswith('\\'):
            full_source = user_vars['base_game_path'] + dirname
        else:
            full_source = user_vars['base_game_path'] + DIR_DELIM + dirname

        full_dest = tmp_game_dir + dirname
        copytree(full_source,full_dest)

    # select mod from list
    print('Please select a mod to run by entering the number associated with the mod:')
    print('\n'.join([f'\t{i}: {mod_names[i]},' for i in range(len(mod_names))])+'\n')
    mod_choice = -1
    while mod_choice < 0 and mod_choice < len(mod_names):
        try:
            mod_choice = int(input('>>> '))
        except:
            print('Not a mod choice, choose again')

    print(f'Preparing and running mod: {mod_names[mod_choice]}')

    # copy mod from list into tmp folder
    mod_files = next(os.walk('mods'+DIR_DELIM+mod_names[mod_choice]))
    mod_filenames, mod_dirs = mod_files[2], mod_files[1]
    mod_source_dir = BASE_DIR + DIR_DELIM + 'mods' + DIR_DELIM + mod_names[mod_choice] + DIR_DELIM

    # files
    for filename in mod_filenames:
        source = mod_source_dir + filename
        dest = tmp_game_dir + filename
        copyfile(source,dest)

    # dirs
    for dirname in mod_dirs:
        source = mod_source_dir + dirname
        dest = tmp_game_dir + dirname
        copytree(source,dest)

    # run the game
    os.system(tmp_game_dir + 'Among Us.exe')





if __name__=='__main__':
    main()

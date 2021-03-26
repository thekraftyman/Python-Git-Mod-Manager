# misc.py
# By: Adam Kraft

'''
A bunch of misc functions for the mod manager
'''

import json
import core.globals as global_vars

# init global vars
global_vars.initialize()

def load_json(filename):
    # open and read the existing json
    with open(filename, 'r') as infile:
        json_dic = json.load(infile)
    return json_dic

def save_json(filename, dictionary):
    # save dictionary to jsons
    with open(filename, 'w+') as outfile:
        json.dump(dictionary,outfile)

def trailing_slash(string):
    # returns the string with the appropriate trailing slash(es)
    if not string.endswith(global_vars.DIR_DELIM):
        string = string + global_vars.DIR_DELIM

    return string

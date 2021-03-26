#!/usr/local/bin/python3
# mod.py
# By: Adam Kraft

'''
A mod class that includes everything a mod should know/do
'''
from core.git_repo import GitRepo
from shutil import copyfile, rmtree, copytree
import core.globals as global_vars

# init the global vars
global_vars.initialize()


class Mod(GitRepo):

    def __init__(self, name, order_number, repo_url, repo_path, parent_path, branch = "Master", debug = False):
        # call paren't init
        super().__init__(repo_url, repo_path, parent_path, branch, debug)

        # continue init of mod
        self.name = name
        self.order_number = order_number


    def load_in_dir(self, destination):
        """
        Copies the mod and moves the copy to the selected destination. 'dumps' files into the dir
        """

        # get all files
        mod_files = next(os.walk(self.path))
        mod_filenames = mod_files[2]
        mod_dirs = mod_files[1]
        mod_source_dir = trailing_slash(self.path)

        # copy files
        for filename in mod_filenames:
            source = mod_source_dir + filename
            dest = destination + filename
            copyfile(source,dest)

        # copy dirs
        for dirname in mod_dirs:
            source = mod_source_dir + dirname
            dest = destination + dirname
            copytree(source,dest)

    def load_to_dir(self, destination):
        """
        Copies the mod and moves the copy to the selected destination. copies to a dir with the same name as the original
        """
        copytree(self.path,dest)

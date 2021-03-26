#!/usr/local/bin/python3
# git_repo.py
# By: Adam Kraft

'''
A class that can leverage git, will be used as a parent for other classes
'''
import git
import os

class GitRepo:

    def __init__(self, repo_url, repo_path, parent_path, branch = "Master", debug = False):
        # init vars
        self._repo_url = repo_url
        self._branch = branch
        self._path = repo_path
        self._parent_path = parent_path
        self._debug = debug
        self._repo = None
        self._cloned = False

        # init the git repo
        self._git_init()

    def _git_init(self):
        """
        Leverages git to download or load git into the repo class
        """

        # Check that the parent path exists
        if not os.path.exists(self._parent_path):
            raise Exception(f'Path {self._parent_path} does not exist')
            exit()

        # Check if the repo path is populated or not
        if not os.path.exists(self._path):
            # doesn't exist, clone
            if self._debug:
                print(f'Repo doesn\'t exist, cloning at {self._path}')
            git.Repo.clone_from(self._repo_url, self._path)
            self._cloned = True

        # load the repo
        if self._debug:
            print(f'Loading repo from path: {self._path}')
        self._repo = git.Repo(self._path)

        # check for loaded data
        if self._repo.bare:
            raise Exception('Could not load repo: {self._repo_url} at location {self._path}')
            exit()

        # make sure we're on the right branch
        branch_res = self._repo.git.checkout(self._branch)
        if not branch_res:
            raise Exception("Could not change to correct branch of repo")

        # Make sure we're up to date (skip if just cloned)
        if not self._cloned:
            self.update()

    @property
    def path(self):
        ''' returns self._path '''
        return self._path


    def update(self):
        """
        Updates the code in the repo to the latest version
        """
        # only update if update is available
        if self._debug:
            print("Checking for updates...")

        if self.check_update():
            if self._debug:
                print("\tUpdate found, pulling...")
            self._repo.remotes.origin.pull()
        else:
            if self._debug:
                print("\tNo updates found!")


    def check_update(self):
        """
        Checks for an update

        Returns
        -------
        bool
            true if update is available, else false
        """

        # fetch origin
        fetch_res = self._repo.remotes.origin.fetch()

        # get last commit saved locally
        commits = self._repo.iter_commits()
        last_commit = [i for i in commits][0]

        # return comparison of last commit and fetched changes
        return fetch_res[0].commit != last_commit

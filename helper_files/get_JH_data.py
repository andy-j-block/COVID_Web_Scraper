
from git import Git

def get_JH_data(JH_data_dir):
    
    #####################
    #
    # This function uses the GitPython module to perform a git pull at the desired
    # directory location, which in this case is the JH_data_dir.
    #
    #####################
    
    g = Git(JH_data_dir)
    g.pull()
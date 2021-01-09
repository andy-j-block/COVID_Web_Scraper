
import subprocess


def get_JH_data(git_bash_exe, helper_files_dir, JH_data_dir):
    
    #####################
    #
    # This function uses the subprocess module to open a git bash instance located
    # at git_bash_exe.  It then loads the git_pull_script shell file that simply
    # performs a git pull in the JH_data_dir directory.  The context manager
    # waits until the process completes and then closes it.
    #
    #####################
    
    with subprocess.Popen([git_bash_exe, helper_files_dir+'/git_pull_script.sh'], \
                           cwd = JH_data_dir) as git_pull:
        
        git_pull.wait()
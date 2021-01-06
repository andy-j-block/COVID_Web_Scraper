
####### TODO
#
# write function description

import subprocess


def get_JH_data(git_bash_exe, helper_files_dir, JH_data_dir):
    
    with subprocess.Popen([git_bash_exe, helper_files_dir+'/git_pull_script.sh'], \
                           cwd = JH_data_dir) as git_pull:
        
        git_pull.wait()
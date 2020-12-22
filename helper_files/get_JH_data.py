
import subprocess


def get_JH_data(helper_files_dir, JH_data_dir):
    
    git_exe = 'C:/Program Files/Git/git-bash.exe'
    
    with subprocess.Popen([git_exe, helper_files_dir+'git_pull_script.sh'], \
                           cwd = JH_data_dir) as git_pull:
        
        git_pull.wait()
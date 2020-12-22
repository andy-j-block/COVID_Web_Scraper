
import subprocess


def get_JH_data(root_dir, helper_files_dir):

    ##################
    
    
    def git_pull(root_dir, helper_files_dir):
    
        git_exe = 'C:/Program Files/Git/git-bash.exe'
        
        with subprocess.Popen([git_exe, helper_files_dir+'git_pull_script.sh'], \
                                    cwd = root_dir) as git_pull:
            git_pull.wait()
      
        
    ##################
    
    git_pull(root_dir, helper_files_dir)
    
    
    ##################
    
    
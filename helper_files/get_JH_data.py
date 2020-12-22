
import subprocess


def get_JH_data(root_dir, helper_files_dir, JH_data_dir):

    ##################
    
    
    def git_pull(root_dir, helper_files_dir, JH_data_dir):
    
        git_exe = 'C:/Program Files/Git/git-bash.exe'
        
        with subprocess.Popen([git_exe, helper_files_dir+'git_pull_script.sh'], \
                               cwd = JH_data_dir) as git_pull:
            git_pull.wait()
      
        
    ##################
    
    git_pull(root_dir, helper_files_dir)
    
    
    ##################
    
    # 2.1 - get latest csv and date of current pull
        
    # root -> down to where our daily csv's are pulled
    daily_files_dir = JH_data_dir + '/csse_covid_19_data/csse_covid_19_daily_reports'
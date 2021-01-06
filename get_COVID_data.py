#############
#
# COVID Web Scraping Tool
#
# Written by Andy Block
# August 18, 2020
#
#############


import os
import pandas as pd
from helper_files.get_dirs import get_dirs
from helper_files.get_git_bash_exe import get_git_bash_exe
from helper_files.get_todays_date import get_todays_date
from helper_files.get_CTP_data import get_CTP_data
from helper_files.get_JH_data import get_JH_data
from helper_files.create_JH_master import create_JH_master
from helper_files.update_JH_master import update_JH_master



if __name__== '__main__':
    
    root_dir, helper_files_dir, CTP_data_dir, JH_data_dir = get_dirs()
    
    git_bash_exe = get_git_bash_exe()
    
    current_day, current_month = get_todays_date()
    
    ##########
        
    get_CTP_data(root_dir, CTP_data_dir, current_month, current_day)
    
    ##########
    
    get_JH_data(git_bash_exe, helper_files_dir, JH_data_dir)
    
    ##########
    
    root_files = os.listdir(root_dir)
    existing_JH_master = [x for x in root_files if 'JH_master' in x]
    
    if len(existing_JH_master) != 1:
        JH_master = create_JH_master(JH_data_dir)
    else:
        JH_master = pd.read_csv(existing_JH_master[0])
    
    update_JH_master(JH_master, JH_data_dir, root_dir)
    
    ##########
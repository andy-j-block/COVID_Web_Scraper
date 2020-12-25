#############
#
# COVID Web Scraping Tool
#
# Written by Andy Block
# August 18, 2020
#
#############
# Preconditions first
#
# 0.1 - define OS specifics, check dir contents
#
# 0.2 - define current day/month/year
#
##############
# COVID Tracking Project
#
# 1.1 - define downloads path and remove any existing daily files
# 1.2 - set up web driver, check for correct versioning
# 1.3 - find the correct link and download daily file
# 1.4 - move file from downloads to root dir
#
#############
# Git
#
# 2.0 - git pull process
# 2.1 - get latest csv and date of current pull
# 2.2 - establish master list file
# 2.3 - find out when last pull took place from last entry in master
# 2.4 - determine list of csv's needed to be appended onto master
# 2.5 - reformat csv's in order from day after last pull to current day
# 2.6 - append master with csv contents in daily order
# 2.7 - save new master file, title in '_month_day.csv' format
#
############


#############
# all imports at top

import os
import pandas as pd
from helper_files.get_dirs import get_dirs
from helper_files.get_executables import get_executables
from helper_files.get_todays_date import get_todays_date
from helper_files.create_webdriver import create_webdriver
from helper_files.get_CTP_data import get_CTP_data
from helper_files.get_JH_data import get_JH_data
from helper_files.create_JH_master import create_JH_master
from helper_files.update_JH_master import update_JH_master



if __name__== '__main__':
    
    root_dir, helper_files_dir, downloads_dir, CTP_data_dir, JH_data_dir = get_dirs()
    
    chrome_exe, git_bash_exe = get_executables()
    
    current_day, current_month = get_todays_date()
    
    
    ##########
    
    driver, escape = create_webdriver(chrome_exe, helper_files_dir, downloads_dir)

########### FIX ESCAPE FUNCTIONALITY
    
    if escape is True:
        error = print('The correct ChromeDriver version was not downloaded and the program cannot continue.')
        return error
        
    get_CTP_data(driver, root_dir, downloads_dir, CTP_data_dir, current_month, current_day)
    
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
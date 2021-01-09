
import os

def get_dirs():
    
    #####################
    #
    # This function get the directory locations for several widely used directories
    # used throughout the script.  The root_dir is the default location where the
    # main script is run from, the helper_files_dir is where all the helper functions
    # are stored, CTP_data_dir is where the COVID Tracking Project daily files 
    # are stored, and the JH_data_dir is where the Johns Hopkins daily files are
    # stored.
    #
    #####################
    
    root_dir = os.getcwd()
    
    helper_files_dir = root_dir + '/helper_files'
    
    CTP_data_dir = root_dir + '/CTP_data'
    
    JH_data_dir = root_dir + '/JH_data/csse_covid_19_data/csse_covid_19_daily_reports'
    
    return root_dir, helper_files_dir, CTP_data_dir, JH_data_dir
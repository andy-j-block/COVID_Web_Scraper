import os

def get_dirs():
    
    root_dir = os.getcwd()
    
    helper_files_dir = root_dir + '/helper_files'
    
    downloads_dir = os.getcwd().split('\\')[:3]
    downloads_dir = '/'.join(downloads_dir) + '/Downloads'
    
    CTP_data_dir = root_dir + '/CTP_data'
    
    JH_data_dir = root_dir + '/JH_data'
    
    return root_dir, helper_files_dir, downloads_dir, CTP_data_dir, JH_data_dir
import os

def get_dirs():
    
    root_dir = os.getcwd()
    
    helper_files_dir = root_dir + '/helper_files'
    
    downloads_dir = os.getcwd().split('\\')[:3]
    downloads_dir = '/'.join(downloads_dir) + '/Downloads'
    
    return root_dir, helper_files_dir, downloads_dir
import os
#import tkinter as tk
#from tkinter import messagebox
#from tkinter import filedialog

def get_dirs():
    
    root_dir = os.getcwd()
    
    helper_files_dir = root_dir + '/helper_files'
    
    # downloads_dir = os.getcwd().split('\\')[:3]
    # downloads_dir = '/'.join(downloads_dir) + '/Downloads'
    
    # if not os.path.exists(downloads_dir):
    #     tk.Tk().withdraw()
    #     error_message = 'Downloads folder not found in the default Windows location. Please identify the location of your Downloads folder in the following file dialog.'
    #     messagebox.showerror('Downloads folder not found',
    #                          error_message)
    #     downloads_dir = filedialog.askopenfilename()
    
    CTP_data_dir = root_dir + '/CTP_data'
    
    JH_data_dir = root_dir + '/JH_data/csse_covid_19_data/csse_covid_19_daily_reports'
    
    return root_dir, helper_files_dir, CTP_data_dir, JH_data_dir
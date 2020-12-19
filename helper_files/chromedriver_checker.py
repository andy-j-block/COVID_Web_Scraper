###########
#
# This function checks the selenium chrome driver version against the installed
# version of chrome on the host machine.  They must be matching in order to run
# the webscraper.
#
###########

###########
#

import os
import tkinter as tk
from tkinter import messagebox
from selenium import webdriver
from win32api import GetFileVersionInfo, HIWORD
from zipfile import ZipFile

def chromedriver_checker(main_dir, helper_files_dir):
    
    # determine chrome version number on host machine, only works for windows
    
    default_locs = ['C:\Program Files (x86)\Google\Chrome\Application\chrome.exe',
                    'C:\Program Files\Google\Chrome\Application\chrome.exe']
    
    if os.path.exists(default_locs[0]):
        chrome_loc = default_locs[0]
    else:
        chrome_loc = default_locs[1]
    
    info = GetFileVersionInfo(chrome_loc,'\\')
    chrome_ver = str(HIWORD(info['FileVersionMS']))
    
    
    # determine if chromedriver version number is equal to chrome version number
    main_dir = os.getcwd() # remove this later
    helper_files_dir = os.getcwd() + '/helper_files/' # remove this later
    
    helper_files = os.listdir(helper_files_dir)
    
    chromedriver = [x for x in helper_files if 'chromedriver_v' in x][0]
    chromedriver_ver= chromedriver.split('.exe')[0][-2:]
    
    if chrome_ver!=chromedriver_ver:
        tk.Tk().withdraw()
        messagebox.showerror('Chrome/ChromeDriver version mismatch',
                            'Your installed Chrome version is v' +chrome_ver+'. Go here to download the corresponding ChromeDriver version: https://chromedriver.chromium.org/downloads')
    else:
        pass
    
    

    # determine if user downloaded chromedriver zip
    downloads_folder = os.getcwd().split('\\')[:3]
    downloads_folder = '/'.join(downloads_folder) + '/Downloads/'
    
    os.path.exists('chromedriver_win32.zip')
        
    
    #driver = webdriver.Chrome(helper_files_dir+chromedriver)
    
    # find the chromedriver
    # 1) check to see if new chromedriver file exists in main dir, helper file dir
    # 2) if none exists, check downloads folder for zip file, copy contents in helper file dir.
    
    #if 'chromedriver.exe' in helper_files_dir: 
        #driver = webdriver.Chrome(main_dir+'chromedriver')
                                  
    #elif 'chromedriver.exe' in main_dir:
        #driver = webdriver.Chrome(helper_files_dir+'chromedriver')
    
                                  
    downloads_folder = os.getcwd().split('\\')[:3]
    downloads_folder = '/'.join(downloads_folder) + '/Downloads/'
    
    with ZipFile(downloads_folder+'chromedriver_win32.zip', 'r') as zip_file:
        zip_file.extract('chromedriver.exe', helper_files_dir)
        
    
    

#chromedriver_checker(os.getcwd() + '/helper_files/')
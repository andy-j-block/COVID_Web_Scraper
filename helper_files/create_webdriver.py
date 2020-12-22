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

def create_webdriver(helper_files_dir, downloads_dir):
    
    ##############
    
    # determine chrome version number on host machine, only works for windows
    
    def get_chrome_version():
    
        default_locs = ['C:\Program Files (x86)\Google\Chrome\Application\chrome.exe',
                        'C:\Program Files\Google\Chrome\Application\chrome.exe']
        
        if os.path.exists(default_locs[0]):
            chrome_loc = default_locs[0]
        else:
            chrome_loc = default_locs[1]
        
        info = GetFileVersionInfo(chrome_loc,'\\')
        chrome_ver = str(HIWORD(info['FileVersionMS']))
        return chrome_ver
    
    ###############
    
    chrome_ver = get_chrome_version()
    
    
    
    ###############
    
    # test chrome_driver, are versions matched?
    # - if yes, simply return driver
    # - if no, tell user to download new version, navigate to zip file,
    #   delete existing chromedriver, extract new chromedriver from zip, 
    #   copy new chromedriver to helper files dir, create driver
    
    def test_chromedriver(helper_files_dir, downloads_dir):
        
        try:
            driver = webdriver.Chrome(helper_files_dir+'/chromedriver.exe')
            return driver
        
        except:
        
            tk.Tk().withdraw()
            error_message = 'Your installed Chrome version is v' +chrome_ver+'. Go here to download the corresponding ChromeDriver version: https://chromedriver.chromium.org/downloads'
            messagebox.showerror('Chrome/ChromeDriver version mismatch',
                                 error_message)
            
            downloads_files = os.listdir(downloads_dir)
            chromedriver_zip = [x for x in downloads_files if 'chromedriver' in x][0]
            
            with ZipFile(chromedriver_zip, 'r') as zip_file:
                os.remove(helper_files_dir+'chromedriver.exe')
                zip_file.extract('chromedriver.exe', helper_files_dir)
            
            driver = webdriver.Chrome(helper_files_dir+'/chromedriver.exe')
            return driver 
     
    ################
    
    
    driver = test_chromedriver(helper_files_dir, downloads_dir)
    return driver

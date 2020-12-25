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

def create_webdriver(chrome_exe, helper_files_dir, downloads_dir):
    
    ##############
    
    # determine chrome version number on host machine, only works for windows
    
    def get_chrome_version(chrome_exe):
        
        try:
            info = GetFileVersionInfo(chrome_exe, '\\')
            chrome_ver = str(HIWORD(info['FileVersionMS']))
            
            windows_TF = True
            
            return chrome_ver, windows_TF
        
        except:
            
            chrome_ver = None
            windows_TF = False
            
            return chrome_ver, windows_TF
    
    ###############
    
    chrome_ver, windows_TF = get_chrome_version(chrome_exe)
    
    
    
    ###############
    
    # test chrome_driver, are versions matched?
    # - if yes, simply return driver
    # - if no, tell user to download new version, navigate to zip file,
    #   delete existing chromedriver, extract new chromedriver from zip, 
    #   copy new chromedriver to helper files dir, create driver
    
    _ = 0
    
    def test_chromedriver(chrome_ver, windows_TF, helper_files_dir, downloads_dir, _):
      
        try:
            driver = webdriver.Chrome(helper_files_dir+'/chromedriver.exe')
            escape = False
            return driver, escape
        
        except:

    ########## driver.quit()??
    
            tk.Tk().withdraw()
            
            if windows_TF is True:
                error_message = 'Your installed Chrome version is v' +chrome_ver+'. Please download the corresponding ChromeDriver version here: https://chromedriver.chromium.org/downloads'
            
            else:
                error_message = 'Please check your Chrome version by opening up your browser settings and selecting the "About Chrome" tab.  The corresponding ChromeDriver version can be found here: https://chromedriver.chromium.org/downloads'
            
            messagebox.showerror('Chrome/ChromeDriver version mismatch',
                                 error_message)
            
            downloads_files = os.listdir(downloads_dir)
            chromedriver_zip = [x for x in downloads_files if 'chromedriver' in x][0]
            
            with ZipFile(chromedriver_zip, 'r') as zip_file:
                os.remove(helper_files_dir+'chromedriver.exe')
                zip_file.extract('chromedriver.exe', helper_files_dir) 

            _ += 1
            
            if _ < 4:             
                escape = False
            else:
                escape = True
                return driver, escape
   
            test_chromedriver(chrome_ver, windows_TF, helper_files_dir, downloads_dir, _)
     
    ################
    
    
    driver, escape = test_chromedriver(chrome_ver, windows_TF, helper_files_dir, downloads_dir, _)
    return driver, escape
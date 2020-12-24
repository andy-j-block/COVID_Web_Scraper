
import os.path
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

def get_executables():
    
    windows_chrome_locs = ['C:\Program Files (x86)\Google\Chrome\Application\chrome.exe',
                           'C:\Program Files\Google\Chrome\Application\chrome.exe']
        
    if os.path.exists(windows_chrome_locs[0]):
        chrome_exe = windows_chrome_locs[0]
        
    elif os.path.exists(windows_chrome_locs[1]):
        chrome_exe = windows_chrome_locs[1]
        
    else:
        tk.Tk().withdraw()
        error_message = 'Chrome executable not found in default Windows locations. Please identify the location of your Chrome executable in the following file dialog.'
        messagebox.showerror('Chrome executable not found',
                             error_message)
        chrome_exe = filedialog.askopenfilename()
        
    
    windows_git_loc = 'C:/Program Files/Git/git-bash.exe'
    
    if os.path.exists(windows_git_loc):
        git_bash_exe = windows_git_loc
    
    else:
        tk.Tk().withdraw()
        error_message = 'Git bash executable not found in default Windows location. Please identify the location of your Git bash executable in the following file dialog.'
        messagebox.showerror('Git bash executable not found',
                             error_message)
        git_bash_exe = filedialog.askopenfilename()
    
    return chrome_exe, git_bash_exe
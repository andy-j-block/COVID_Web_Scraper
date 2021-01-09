
import os.path
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

def get_git_bash_exe():
    
    ####################
    #
    # This function takes the git bash executable and stores its location as a 
    # variable (git_bash_exe).  It first tries to use the default windows location
    # for the git bash executable and if it does not exist there, a filedialog
    # box is opened for the user to select the location manually. 
    #
    ####################
    
    windows_git_loc = 'C:/Program Files/Git/git-bash.exe'
    
    if os.path.exists(windows_git_loc):
        git_bash_exe = windows_git_loc
    
    else:
        tk.Tk().withdraw()
        error_message = 'Git bash executable not found in default Windows location. Please identify the location of your Git bash executable in the following file dialog.'
        messagebox.showerror('Git bash executable not found',
                             error_message)
        git_bash_exe = filedialog.askopenfilename()
    
    return git_bash_exe
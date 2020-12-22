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

import pandas as pd
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import subprocess
from helper_files.create_webdriver import create_webdriver
from helper_files.get_dirs import get_dirs
from helper_files.get_CTP_data import get_CTP_data
import os
import os.path


#############

root_dir, helper_files_dir, downloads_dir, CTP_data_dir, JH_data_dir = get_dirs()

##############
# 0.2 - define current day/month/year
from datetime import date    

current_date = str(date.today())
current_day = current_date.split('-')[2]
current_month= current_date.split('-')[1]
current_year= current_date.split('-')[0]


###########

driver = create_webdriver(helper_files_dir, downloads_dir)

#get_CTP_data(driver, downloads_dir)

    
###############
#    
# Johns Hopkins Github
#
############
#
# 2.1 - get latest csv and date of current pull
# 2.2 - establish master list file
# 2.3 - find out when last pull took place from last entry in master
# 2.4 - determine list of csv's needed to be appended onto master
# 2.5 - reformat csv's in order from day after last pull to current day
# 2.6 - append master with csv contents in daily order
# 2.7 - save new master file, title in '_month_day.csv' format
#
#############


#############
# 2.1 - get latest csv and date of current pull

# root -> down to where our daily csv's are pulled
down_two = '/csse_covid_19_data/csse_covid_19_daily_reports'

if os.path.isdir(root_path+'/COVID-19'):
    down_two='/COVID-19'+down_two

git_files_dir = root_path + down_two


##########
# 2.2 - establish master list file

# get root directory contents
root_contents = os.listdir(root_path)

# check to see if master list exists already
master_file = ''
for x in root_contents:
    if 'master' in x:
        master_file = root_path+'/'+x
    else:
        continue

# if no files in root dir contain the word master, open selection to find one
if master_file=='':
    
    # first run, request master file
    
    master_select = tk.Tk()
    master_select.withdraw()
    
    messagebox.showinfo("Master File Not Found in Root Dir", \
                        "You will now be prompted to select existing master list")
    
    original_master_path = filedialog.askopenfilename(initialdir=root_path, \
                                                      title = "Select existing master file")
        
    master_file = original_master_path


##########
# 2.3 - find out when last pull took place from last entry in master

# list of contents in git files folder
all_daily_files = os.listdir(git_files_dir)

# set current day number minus one
current_day_minus_1= str(int(current_day)-1)

# assume newest_file is dated one day prior to pull
newest_file = current_month+'-'+current_day_minus_1+'-'+current_year+'.csv'

# set date of most recent data if newest_file isn't from yesterday
if not os.path.exists(git_files_dir+'/'+newest_file):
    try:
        newest_file = all_daily_files[-2]
        month_num = newest_file.split('-')[0]
        day_num = newest_file.split('-')[1]
        print('Most recent data from '+month_num+'-'+day_num)
    except:
        print('New (non-"date titled") file added to directory,\
              more than just the README and .gitignore.\
              Please remove these additional files.')


#########
# 2.4 - determine list of csv's needed to be appended onto master

import pandas as pd

# read master list in as dataframe
master_df= pd.read_csv(master_file)

# if last update column has a space instead of underscore, let's reformat
if 'Last Update' in master_df.columns:
    master_df= master_df.rename(columns={'Last Update':'Last_Update'})
elif 'Date' in master_df.columns:
    master_df= master_df.rename(columns={'Date':'Last_Update'})
    
# get last entry and separate dateparts
master_last_entry = master_df['Last_Update'].iloc[-1]   

if '-' in master_last_entry:
    master_last_month = master_last_entry.split('-')[1]
    master_last_day = master_last_entry.split('-')[2]
    master_last_year = master_last_entry.split('-')[0]
elif '/' in master_last_entry:
    master_last_month = master_last_entry.split('/')[0]
    master_last_day = master_last_entry.split('/')[1]
    master_last_year = master_last_entry.split('/')[2]

# add leading zero to month and day parts if required
if len(master_last_month) == 1:
    master_last_month = '0'+master_last_month
if len(master_last_day) == 1:
    master_last_day = '0'+master_last_day

master_last = master_last_month+'-'+master_last_day+'-'+master_last_year+'.csv'                           

# get indices of master_last_csv and newest_file within all_daily_files
master_last_idx = all_daily_files.index(master_last)
newest_file_idx = all_daily_files.index(newest_file)

# list of csv's to edit and append
new_csv_files = all_daily_files[master_last_idx+1:newest_file_idx+1]


#########
# 2.5 - reformat csv's in order from day after last pull to current day
# 2.6 - append master with csv contents in daily order

for x in new_csv_files:
    
    # pull in new file as pandas csv
    new_file = pd.read_csv(git_files_dir+'/'+x)
    
    # get day number of csv
    day_num = x.split('-')[1]

    # chop time values off of 'Last_Update' column
    new_file['Last_Update']= \
        new_file['Last_Update'].apply(lambda x: x.split(' ')[0])
    
    # get year and month of current file, e.g. '2020-08-'
    year= x.split('-')[2][:-4]
    month= x.split('-')[0]

    # update 'Last_Update' column with date from file
    file_date = year +'-'+ month +'-'+ day_num
    new_file['Last_Update']= file_date
    
    # append this new daily data to new_data dataframe
    master_df = master_df.append(new_file, ignore_index=True)


    # replace files in git pull directory with edited files
    # nice to have, if hand editing needed later
    # new_file.to_csv(git_files_dir +'/'+ month +'-'+ day_num +'-'+ year +'.csv',\
    #                index=False, header=False)
  
      
#########
# 2.7 - remove old master file, save new master file, title in '_month_day.csv' format

# remove existing master file to be replaced, unless there are no new csv files
if not new_csv_files==[] and 'master.csv' in master_file:
    os.remove(master_file)

# save master dataframe as a csv file, title formatted to date of last available data
master_df.to_csv(root_path + '/master.csv', index=False)

# save master dataframe as a daily copy
masters_dir = root_path + '/Historical Master Files'

if not os.path.isdir(masters_dir):
    os.mkdir(masters_dir)

if not new_csv_files==[]:    
    master_df.to_csv(masters_dir + '/master_' + month+'_'+day_num + '.csv', index=False)


#if __name__== '__main__':
    
    # root_dir, helper_files_dir, downloads_dir = get_dirs()
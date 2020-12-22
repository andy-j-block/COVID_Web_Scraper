
import pandas as pd


def update_JH_master(JH_master):
    
    ####################
    
    def reformat_datetime(JH_master):
        
        JH_master['Last_Update'] = pd.to_datetime(JH_master['Last_Update'], format='%Y-%m-%d %H:%M:&S')
        JH_master['Last_Update'] = JH_master['Last_Update'].dt.date

        JH_master = JH_master.sort_values('Last_Update', ascending = True)
        
        return JH_master
    
    #####################

    
    JH_master = reformat_datetime(JH_master)


    #####################
    
    def get_date_last_pull(JH_master):
        
        last_pull = JH_master['Last_Update'].iloc[-1]
        last_pull = last_pull - pd.Timedelta('1 day')
        
        return last_pull
    
    #####################
    
    
    last_pull = get_date_last_pull(JH_master)
    
    
    #####################
    

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
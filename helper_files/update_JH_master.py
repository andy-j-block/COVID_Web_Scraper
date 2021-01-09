
import pandas as pd
import os
from datetime import date, timedelta


def update_JH_master(JH_master, JH_data_dir, root_dir):
    
    ###################
    #
    # set_datetime():
    # This function changes the 'Last_Update' column to datetime format and removes
    # the time values, leaving only the date.  The column is then sorted from
    # oldest value to newest and the dataframe is returned.
    #
    # get_pull_dates():
    # This function defines the range of dates that need to be imported into the
    # JH_master.csv file.  The funky part here is twofold:
    #
    #   - files uploaded on a given date are labeled as the day prior (pull on
    #     12-15 will have data labelled up to '12-14.csv')
    #   - a file labeled '12-15.csv' actually contains data listed as '12-16'
    #
    # Thus, for a pulls done on 12-15 and 12-20, the new files begin at '12-15.csv' 
    # and stretch until 12-20 but minus one day ('12-19.csv').
    #
    # add_new_data():
    # This function adds the newly pulled JH data and concatenates it onto the
    # JH_master dataframe file by file.  First it defines the range of files to
    # be added, and then they are iterated thru, datetime conversions are performed,
    # and the data is concatenated onto the dataframe.  Lastly, if new files were
    # present, the new JH_master dataframe is saved to file, else the function
    # ends.
    #
    ###################
    
    ####################
    
    def set_datetime(JH_master):
        
        JH_master['Last_Update'] = pd.to_datetime(JH_master['Last_Update'])
        JH_master['Last_Update'] = JH_master['Last_Update'].dt.date

        JH_master = JH_master.sort_values('Last_Update', ascending = True)
        
        return JH_master
    
    #####################

    
    JH_master = set_datetime(JH_master)


    #####################
    
    def get_pull_dates(JH_master):
        
        last_pull = JH_master['Last_Update'].iloc[-1]
        
        last_pull = last_pull - pd.Timedelta('1 day')
        
        last_pull = last_pull.strftime('%m-%d-%Y')
        
        last_pull = last_pull + '.csv'
        
        # today's pull is labelled as yesterday's date
        
        todays_pull = date.today() - timedelta(days=1)
        
        todays_pull = todays_pull.strftime('%m-%d-%Y')
        
        todays_pull = todays_pull + '.csv'
        
        return last_pull, todays_pull
    
    #####################
    
    
    last_pull, todays_pull = get_pull_dates(JH_master)
    
    
    #####################
    
    def add_new_data(JH_master, last_pull, todays_pull, JH_data_dir, root_dir):
        
        # identify csv's to add to master
        JH_files = os.listdir(JH_data_dir)[1:-1]
        
        new_JH_files = JH_files[JH_files.index(last_pull)+1:
            JH_files.index(todays_pull)+1]
            
        new_JH_files = [JH_data_dir + '/' + x for x in new_JH_files]
        
        for i in new_JH_files:
            
            new_data = pd.read_csv(i)
            
            new_data['Last_Update'] = pd.to_datetime(new_data['Last_Update'])
            
            new_data['Last_Update'] = new_data['Last_Update'].dt.date
        
            JH_master = pd.concat([JH_master, new_data], ignore_index=True)
        
        if new_JH_files != []:
            JH_master.to_csv(root_dir + '/JH_master.csv')

    #####################
    
    add_new_data(JH_master, last_pull, todays_pull, JH_data_dir, root_dir)

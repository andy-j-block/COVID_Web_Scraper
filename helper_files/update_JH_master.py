
import pandas as pd
import os
from datetime import date, timedelta


def update_JH_master(JH_master, JH_data_dir, root_dir):
    
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
        
        new_JH_files = JH_files[JH_files.index(last_pull):
            JH_files.index(todays_pull)+1]
            
        new_JH_files = [JH_data_dir + '/' + x for x in new_JH_files]
        
        for i in new_JH_files:
            
            new_data = pd.read_csv(i)
            
            new_data['Last_Update'] = pd.to_datetime(new_data['Last_Update'])
            
            new_data['Last_Update'] = new_data['Last_Update'].dt.date
        
            JH_master = pd.concat([JH_master, new_data], ignore_index=True)
        
        JH_master.to_csv(root_dir + '/JH_master.csv')

    #####################
    
    add_new_data(JH_master, last_pull, todays_pull, JH_data_dir, root_dir)

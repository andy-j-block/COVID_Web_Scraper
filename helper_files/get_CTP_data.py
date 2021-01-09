import os
import os.path
import requests


def get_CTP_data(root_dir, CTP_data_dir, current_month, current_day):
    
    
    #################
    #
    # This function uses the requests package to directly call the COVID Tracking
    # Project's data API and pull its contents.  These contents are saved to the
    # root dir as 'CTP_daily.csv' and an additional copy is saved to the CTP_data_dir
    # subfolder with a dated title.  For instance, a file pulled on December 15th
    # would be saved to the CTP_data_dir as 'CTP_daily-12-15.csv'.
    #
    # The call to the API can sometimes timeout so it's been bulletproofed with
    # a while loop that will repeat until the new file exists in the root_dir.
    #
    #################
          
    new_daily_file = root_dir + '/CTP_daily.csv'
    
    dated_filename = '/CTP_daily_' + current_month + '-' + current_day + '.csv'
    dated_daily_file = CTP_data_dir + dated_filename
    
    while not os.path.exists(new_daily_file):
        try:
            r = requests.get('https://api.covidtracking.com/v1/states/daily.csv', timeout=5)
            
        except:
            continue
        
        with open(dated_daily_file, 'wb') as f1:
            f1.write(r.content)
        
        with open(new_daily_file, 'wb') as f2:
            f2.write(r.content)
            

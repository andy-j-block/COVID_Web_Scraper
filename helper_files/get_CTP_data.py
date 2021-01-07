import os
import os.path
import requests


def get_CTP_data(root_dir, CTP_data_dir, current_month, current_day):
    
    
    #################
    #
    # This function first changes the downloaded 'daily.csv' file to a dated
    # filename, i.e. 'CTP_daily_12-20.csv' for a daily file downloaded on Dec 20.
    # It then moves the previous daily file from the root directory to the 
    # CTP_data directory. Finally, it moves the new, dated file from the 
    # downloads directory to the root directory.
    #
    #################
          
    new_daily_file = root_dir + '/CTP_daily.csv'
    
    dated_filename = '/CTP_daily_' + current_month + '-' + current_day + '.csv'
    dated_daily_file = CTP_data_dir + dated_filename
    
    while not os.path.exists(new_daily_file):
        try:
            r = requests.get('https://api.covidtracking.com/v1/states/daily.csv',
                             timeout=5)
            
        except:
            continue
        
        with open(dated_daily_file, 'wb') as f1:
            f1.write(r.content)
        
        with open(new_daily_file, 'wb') as f2:
            f2.write(r.content)
            

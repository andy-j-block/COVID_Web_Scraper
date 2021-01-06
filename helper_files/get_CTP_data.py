import os
import os.path
import shutil
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
    
    
    # move existing daily file to CTP_data dir (if it exists)
        
    root_dir_files = os.listdir(root_dir)
    existing_daily = [x for x in root_dir_files if 'CTP_daily' in x]
    
    if len(existing_daily) == 1:      
        shutil.move(root_dir +'/'+ existing_daily[0], CTP_data_dir +'/'+ existing_daily[0])
    
    
    
    dated_filename = '/CTP_daily_' + current_month + '-' + current_day + '.csv'
    
    new_daily_file = root_dir+dated_filename
    
    while not os.path.exists(new_daily_file):
        try:
            r = requests.get('https://api.covidtracking.com/v1/states/daily.csv', timeout=5)
        except:
            continue
        
        with open(new_daily_file,'wb') as f:
            f.write(r.content)
    
    

    
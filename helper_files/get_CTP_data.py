import os
import os.path
import time
import shutil


def get_CTP_data(driver, root_dir, downloads_dir, CTP_data_dir, current_month, current_day):
    
    
    #################
    # 
    # This function gets the latest daily cases file from the COVID Tracking
    # Project's API by navigating to the website, clicking the 'histotical data
    # for all states' dropdown, and clicking the link to the csv file.
    #
    # There is also a timeout protection in case the API doesn't respond and 
    # the request needs to be made again.
    #
    
    def get_latest_daily(driver, downloads_dir):
    
        timer=0
        
        # remove any daily files if they exist
        try:
            os.remove(downloads_dir+'/daily.csv')
        except:
            pass
    
    
        while not os.path.exists(downloads_dir+'/daily.csv'):
            
            # navigate to website
            covid_tracking_proj= 'https://covidtracking.com/data/api'
            driver.get(covid_tracking_proj)
            
            # click 'historical data for all states' dropdown
            dropdown_xpath= '//button[@aria-controls="panel--6"]'
            driver.find_element_by_xpath(dropdown_xpath).click()
            
            # click link to csv file to download
            link_text= 'https://api.covidtracking.com/v1/states/daily.csv'
            driver.find_element_by_link_text(link_text).click()
            
            while not os.path.exists(downloads_dir+'/daily.csv'):
                time.sleep(1)
                timer += 1
                # restart process after 5 seconds because something timed out
                if timer % 5 == 0:
                    driver.execute_script('window.stop();')
                    break
        
        # close chrome
        driver.quit()
    
    #################
    
    
    get_latest_daily(driver, downloads_dir)
    
    
    #################
    #
    # This function first changes the downloaded 'daily.csv' file to a dated
    # filename, i.e. 'CTP_daily_12-20.csv' for a daily file downloaded on Dec 20.
    # It then moves the previous daily file from the root directory to the 
    # CTP_data directory. Finally, it moves the new, dated file from the 
    # downloads directory to the root directory.
    #
    
    def format_daily(root_dir, downloads_dir, CTP_data_dir, current_month, current_day):
        
        # rename newly-downloaded daily file
        
        default_filename = '/daily.csv'
        dated_filename = '/CTP_daily_' + current_month + '-' + current_day + '.csv'
        
        os.rename(downloads_dir + default_filename, downloads_dir + dated_filename)
        
        
        # move existing daily file to CTP_data dir (if it exists)
        
        root_dir_files = os.listdir(root_dir)
        existing_daily = [x for x in root_dir_files if 'CTP_daily' in x]
        
        if len(existing_daily) == 1:      
            shutil.move(root_dir +'/'+ existing_daily[0], CTP_data_dir +'/'+ existing_daily[0])
        
        # move new file from downloads to root
        
        original_file_loc = downloads_dir + dated_filename
        target_file_loc = root_dir + dated_filename
        
        shutil.move(original_file_loc, target_file_loc)

        
    #################
    
    format_daily(root_dir, downloads_dir, CTP_data_dir, current_month, current_day)
    
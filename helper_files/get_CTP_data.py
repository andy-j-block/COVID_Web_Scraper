import os
import os.path
import time
import shutil


def get_CTP_data(driver, downloads_dir, CTP_data_dir, current_month, current_day):
    
    
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
    # filename, i.e. 'daily_12-20.csv' for a daily file downloaded on Dec 20.
    # It then moves this dated file from the downloads directory to the 
    # CTP data directory.
    #
    
    def format_daily(downloads_dir, CTP_data_dir, current_month, current_day):
        
        default_filename = '/daily.csv'
        dated_filename = '/daily_' + current_month + '-' + current_day + '.csv'
        
        os.rename(downloads_dir + default_filename, downloads_dir + dated_filename)
        
        original_dir = downloads_dir + dated_filename
        target_dir = CTP_data_dir + dated_filename
        
        shutil.move(original_dir, target_dir)
        
        
    #################
    
    format_daily(downloads_dir, CTP_data_dir, current_month, current_day)
    
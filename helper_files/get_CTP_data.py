import os
import os.path
import time
import shutil


def get_CTP_data(driver, downloads_dir):
    
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
                driver.execute_script("window.stop();")
                break
    
    # close chrome
    driver.quit()
    
    
    
    daily_file = '/daily.csv'
    daily_file_w_date = '/daily_'+current_month+'-'+current_day+'.csv'
    shutil.copyfile(downloads_path+daily_file, downloads_path+daily_file_w_date)
    
    # move daily_file to root path as 'daily.csv'
    shutil.move(downloads_path+daily_file, root_path+daily_file)
    # check to make sure daily_file made it to root_path 
    assert os.path.exists(root_path+daily_file),\
        'Daily file did not move to root directory properly, please move manually'
        
    # create daily file directory if one does not exist
    dailys_dir = root_path+'/Historical Daily Files'
    
    if not os.path.isdir(dailys_dir):
        os.mkdir(dailys_dir)
    
    # move daily_file_w_date to '/Daily Files' directory    
    shutil.move(downloads_path+daily_file_w_date, dailys_dir+daily_file_w_date)
import os.path


def get_CTP_data(driver, downloads_dir):

    
    downloads = os.getcwd().split('\\')[:3]
    downloads = '/'.join(downloads) + '/Downloads'
    
    timer=0

    while not os.path.exists(downloads_path+'/daily.csv'):
        
        # navigate to website
        covid_tracking_proj= 'https://covidtracking.com/data/api'
        driver.get(covid_tracking_proj)
        
        # click 'historical data for all states' dropdown
        dropdown_xpath= '//button[@aria-controls="panel--6"]'
        driver.find_element_by_xpath(dropdown_xpath).click()
        
        # click link to csv file to download
        link_text= 'https://api.covidtracking.com/v1/states/daily.csv'
        driver.find_element_by_link_text(link_text).click()
        
        while not os.path.exists(downloads_path+'/daily.csv'):
            time.sleep(1)
            timer += 1
            # restart process after 5 seconds because something timed out
            if timer % 5 == 0:
                driver.execute_script("window.stop();")
                break
    
    # close chrome
    driver.quit()
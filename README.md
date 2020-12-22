# COVID_Web_Scraper
This web scraping tool collects COVID data from two sources (John Hopkins Github and the COVID Tracking Project) , reformats the datetime information, determines what data is new, and appends it into the master dataset.

## Project Intent
This tool was built while at Ford Motor Company for my section's technical specialist Reid.  He was keeping the team up to date on the latest COVID numbers locally and regionally through several Tableau visualizations.  Unfortunately though, the process he was using of manually collecting the data and formatting it properly was consuming a fair amount of his time, especially given that this preprocessing was a once- or twice-weekly process.  Thus, I decided to lend him a hand on this by automating the process and giving me an opportunity to practice my data scraping skills.

## Data Sources
* COVID Tracking Project at the Atlantic - https://covidtracking.com/data/api
* Johns Hopkins COVID-19 Data Repository - https://github.com/CSSEGISandData/COVID-19

## Features
* Directory Check
  * Ensures the user has all the necessary helper files required to run the script and alerts the user through assert statements if a given file is missing from the base directory


## Helper File Explanations

1. [get_dirs](#get_dirs)
2. [create_webdriver](#create_webdriver)
3. [get_CTP_date](#get_CTP_data)

### get_dirs
* This function simply returns the following three directories for use by the other functions in this webscraper:
    ** root_dir - the root directory on the host machine
    ** helper_files_dir - the sub-directory containing all the helper files and modules
    ** downloads_dir - the downloads folder of the host machine
    
### create_webdriver
* This function does two main jobs:
    ** Acquiring the version of Chrome currently installed on the host machine
    ** Creating an instance of the Chromedriver for use in get_CTP_data function

### get_CTP_data
* This function does the hard yards of getting the data, formatting the filename, moving it to where it needs to be, etc.
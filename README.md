# COVID Web Scraper

### Contents
1. [Project Intent](#intent)
2. [Data Sources](#data_sources)
3. [Features](#features)
4. [Helper Function Explanations](#helper_fcns)

## Project Intent  <a name="intent"></a>
This web scraping tool collects COVID data from two sources (John Hopkins Github and the COVID Tracking Project), reformats the datetime information, determines what data is new, and appends it into the master dataset.

This web scraper uses two methods for data collection: using the Selenium module and associated Chromedriver to navigate to the COVID Tracking Project website and pull daily case data from their API, and launching a git shell to pull ____ from the Johns Hopkins COVID19 data repo.

This tool was built while at Ford Motor Company for my section's technical specialist Reid.  He was keeping the team up to date on the latest COVID numbers locally and regionally through several Tableau visualizations.  Unfortunately though, the process he was using of manually collecting the data and formatting it properly was consuming a fair amount of his time, especially given that this preprocessing was a once- or twice-weekly process.  Thus, I decided to lend him a hand on this by automating the process, giving me an opportunity to practice my data scraping skills.

## Data Sources  <a name="data_sources"></a>
* COVID Tracking Project at The Atlantic - https://covidtracking.com/data/api
* Johns Hopkins COVID-19 Data Repository - https://github.com/CSSEGISandData/COVID-19

## Features  <a name="features"></a>
* Directory Check
  * Ensures the user has all the necessary helper files required to run the script and alerts the user through assert statements if a given file is missing from the base directory

## Helper Function Explanations  <a name="helper_fcns"></a>

<details><summary><strong>Functions</strong></summary>
<p>

- *[get_dirs](#get_dirs)*
- *[get_todays_date](#get_todays_date)*
- *[create_webdriver](#create_webdriver)*
- *[get_CTP_data](#get_CTP_data)*
- *[get_JH_data](#get_JH_data)*
- *[create_JH_master](#create_JH_master)*
- *[update_JH_master](#update_JH_master)*

</p>
</details>


### *get_dirs*
This function returns the locations of five directories commonly used throughout 
the program.  The subsequent helper files require many of these directories as 
inputs. The five directory outputs are as follows:

* `root_dir` - the root directory on the host machine
* `helper_files_dir` - the sub-directory containing all the helper files and modules
* `downloads_dir` - the downloads folder of the host machine
* `CTP_data_dir` - the directory where historical daily CTP reports are stored
* `JH_data_dir` - the directory where the JH github repo is stored

The `downloads_dir` directory is the only one located outside of the webscraper's 
repository.  Thus, it has been defaulted to the Downloads folder on Windows.  If
this folder cannot be found (i.e., user running a different OS), the function 
will prompt the user to indentify the location of the host machine's Downloads 
folder.

### *get_executables*
This function allows for easier usage of this webscraper across operating systems 
by identifying the locations of the Chrome browser and Git bash executables.  
It returns the following two variables:

* `chrome_exe`
* `git_bash_exe`

Again, my personal computer runs Windows and thus I've set the locations of these 
executables to their default locations on Windows.  However, if this program is 
run on a non-Windows machine, a warning box will open indicating that the 
executables cannot be found and a file dialog box is subsequently opened in 
which the user can identify their locations.

### *get_todays_date*
This function simply returns the day and month at the time of running the program.  
They are stored as the following variables:

* `current_day`
* `current_month`
  
### *create_webdriver*
This function does two main jobs:
* Acquiring the version of Chrome currently installed on the host machine
* Creating an instance of the Chromedriver for use in get_CTP_data function

### *get_CTP_data*
This function does the hard yards of getting the COVID Tracking Project (CTP) 
data, formatting the filename, moving it to where it needs to be, etc.

### *get_JH_data*
This function performs a git pull on the JH repo stored in the JH_data folder.  
It uses the subprocess module to open a git bash using the executable stored in 
`git_bash_exe`.

### *create_JH_master*
This function creates a new JH_master CSV file if one does not already exist in 
the main root folder.  This will take all of the 

### *update_JH_master*






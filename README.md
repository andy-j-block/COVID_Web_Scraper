# COVID Web Scraper
<div align="justify">   


### Table of Contents
1. [Project Intent](#intent)
2. [Data Sources](#data_sources)
3. [Setup and Running](#setup)
4. [Helper Function Explanations](#helper_fcns)


## Project Intent  <a name="intent"></a>
This web scraping tool collects COVID data from two sources (Johns Hopkins Github and the COVID Tracking Project), reformats the datetime information, determines what data is new, and appends it into the master dataset.

This web scraper uses two methods for data collection: using the Selenium module and associated Chromedriver to navigate to the COVID Tracking Project website and pull daily case data from their API, and launching a git shell to pull ____ from the Johns Hopkins COVID19 data repo.

This tool was built while at Ford Motor Company for my section's technical specialist Reid.  He was keeping the team up to date on the latest COVID numbers locally and regionally through several Tableau visualizations.  Unfortunately though, the process he was using of manually collecting the data and formatting it properly was consuming a fair amount of his time, especially given that this preprocessing was a once- or twice-weekly process.  Thus, I decided to lend him a hand on this by automating the process, giving me an opportunity to practice my data scraping skills.


## Data Sources  <a name="data_sources"></a>
<p style="text-align:center;">
   <img src="CTP_JH_logos.png">
</p>

* COVID Tracking Project at The Atlantic - https://covidtracking.com/data/api
* Johns Hopkins COVID-19 Data Repository - https://github.com/CSSEGISandData/COVID-19

## Setup and Running  <a name="setup"></a>

This Git repo can either be downloaded as a zip or cloned onto your machine.  In order to populate the `JH_data` subfolder, please open a git bash from the main root folder and run `git submodule update --init`.  There is also an `environment.yml` file in the root directory that can be used to clone the conda environment with all the necessary packages to run this program.

The user need only run the `get_COVID_data.py` file in order to run the program, everything else is taken care of by the helper functions.  It performs the following tasks in order:

#### *Initialization*
* gets the directories commonly used in the program and stores their locations as variables
* gets the current day and month and stores those as variables for later use

#### *COVID Tracking Project Data*
* navigates to the COVID Tracking Project's web API and downloads the daily case data
* saves the most recent data into the root directory and moves old data to the `CTP_data` sub-folder

#### *Johns Hopkins Data*
* runs a Git pull on the data stored in the `JH_data` sub-folder using a subprocess and context manager
* scans the root directory for an existing instance of `JH_master.csv` file
    * if none found, a new `JH_master.csv` file is created and populated with all the existing data up to the date of the most recent Git pull
    * if `JH_master.csv` found, read in this data as a pandas dataframe and continue
* sets the `'Last_Update'` column as a datetime and determines the date of the last Git pull
* takes all of the new data since the last Git pull file by file and adds their contents to the `JH_master.csv`
* saves the updated `JH_master.csv` file to the root directory

Please see the following section for a more detailed explanation of all of the helper functions. 


## Helper Function Explanations  <a name="helper_fcns"></a>

<details><summary><strong><em>get_dirs</em></strong></summary>
<p>

This function returns the locations of four directories commonly used throughout the program.  The subsequent helper files require many of these directories as inputs. The four directory outputs are as follows:

* `root_dir` - the root directory on the host machine
* `helper_files_dir` - the sub-directory containing all the helper files and modules
* `CTP_data_dir` - the directory where historical daily CTP reports will be moved to
* `JH_data_dir` - the sub-directory within the JH github repo where the daily reports are stored

</p>
</details>

<details><summary><strong><em>get_todays_date</em></strong></summary>
<p>

This function simply returns the day and month at the time of running the program using the `datetime` module.  They are stored as the following variables:

* `current_day`
* `current_month`

These variables are used in the `get_CTP_data` function for file labeling purposes.

</p>
</details>

<details><summary><strong><em>get_CTP_data</em></strong></summary>
<p>

Fix

This function does the hard yards of getting the COVID Tracking Project (CTP) data, formatting the filename, moving the new data to where it needs to be.

Selenium is powering the driver functionality to navigate within the browser.  After accessing the COVID Tracking Project's website, the driver clicks its way to the link where the target data is stored.

One snag discovered during robustness testing was that sometimes the browser would timeout after requesting data from the API and the data would not be successfully downloaded.  Thus, I implemented my own timer to restart the process if the browser timeout issue occurred.

Since these files contain daily data, the last part of this function will scan the contents of the root directory for an existing daily file and move it to the CTP_data sub-folder if it exists.  It's only at this point that the newly-downloaded daily file is renamed to include the `current_day` and `current_month` (from `get_todays_date` function) and moved to the root directory.

</p>
</details>

<details><summary><strong><em>get_JH_data</em></strong></summary>
<p>

This function performs a Git pull on the JH repo stored in the `JH_data` subfolder.  It uses the `GitPython` module by creating a Git class object, giving it the `JH_data_dir` as the target folder, and using the pull() method to perform the git pull.

</p>
</details>

<details><summary><strong><em>create_JH_master</em></strong></summary>
<p>

This function creates a new `JH_master.csv` file if one does not already exist in the `root_dir`.  It loops thru all of the existing files in the `JH_data`

</p>
</details>

<details><summary><strong><em>update_JH_master</em></strong></summary>
<p>

This function performs three separate tasks:

* Sets the `'Last_Update'` column in the `JH_master` dataframe to a datetime data type and drops the time portion
* Determines the date of the most recent Git pull by shifting the last date entry back by 1 day (i.e. daily files labeled 12-08-2020 contains data dated as 12-09-2020)
* Determines the new data that need to be appended to `JH_master` and loops thru these files, concatenating them to `JH_master`
* Saves the `JH_master` dataframe to the root directory

</p>
</details>




</div> 

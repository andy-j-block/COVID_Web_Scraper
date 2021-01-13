# COVID Web Scraper
<div align="justify">   


### Table of Contents
1. [Project Intent](#intent)
2. [Data Sources](#data_sources)
3. [Setup and Running](#setup)
4. [Helper Function Explanations](#helper_fcns)


## Project Intent  <a name="intent"></a>

This web scraping tool collects COVID data from two sources for use making COVID visualizations and dashboards.

This tool was built while at Ford Motor Company for our team's technical specialist.  He was keeping us up to date on the latest COVID case numbers locally and regionally through several Tableau dashboards, but the process of manually collecting the data and formatting it properly was consuming a fair amount of his time, especially given that this was a once- or twice-weekly process.  Thus, I decided to lend him a hand by automating this process, giving me an opportunity to practice my data scraping skills and providing the team with a functional web scraper that could be employed on future projects.

This program uses two methods for data collection: using HTTP requests to access the COVID Tracking Project's data API and pulling the latest data from the Johns Hopkins COVID19 data repository.

## Data Sources  <a name="data_sources"></a>

<p style="text-align:center;">
   <img src="CTP_JH_logos.png">
</p>

* COVID Tracking Project at The Atlantic (CTP) - https://covidtracking.com/data/api
* Johns Hopkins COVID-19 Data Repository (JH) - https://github.com/CSSEGISandData/COVID-19

## Setup and Running  <a name="setup"></a>

This Git repo can either be downloaded as a zip or cloned onto your machine.  In order to populate the `JH_data` subfolder, please open a git bash from the root directory and run `git submodule update --init`.  There is also an `environment.yml` file in the root directory that can be used to clone the conda environment with all the packages necessary to run this program.

The user need only run the `get_COVID_data.py` file in order to use the web scraper, everything else is taken care of by the helper functions.  It performs the following tasks in order:

#### *Initialization*
* gets the directories commonly used in the program and stores their locations as variables
* gets the current day and month and stores those as variables for later use

#### *COVID Tracking Project Data*
* sends an HTTP request to the COVID Tracking Project's data API and downloads the daily case data
* saves the most recent data in the root directory and also saves a copy in the `CTP_data` sub-folder with a dated filename

#### *Johns Hopkins Data*
* runs a Git pull on the data stored in the `JH_data_dir` sub-folder using the GitPython module
* scans the root directory for an existing instance of `JH_master.csv` file
    * if none are found, a new `JH_master.csv` file is created and populated with all the existing data up to the date of the most recent Git pull
    * if `JH_master.csv` is found, read in this data as a pandas dataframe and continue
* sets the `'Last_Update'` column as a datetime and determines the date of the last Git pull
* takes all of the new data since the last Git pull and adds their contents to the `JH_master.csv` file by file
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

This function accesses the CTP data API via an HTTP request, which returns the latest daily case data.  Two copies of this data are saved:

* one instance is saved to the `root_dir` as `CTP_daily.csv`
* another instance is saved to the `CTP_data_dir` with a dated filename using the `current_month` and `current_day` variables
    * the date formatting of the filename is month-day, so a file downloaded on December 15 would be saved as `CTP_daily_12-15.csv`

Since the data API isn't guaranteed to respond to the HTTP request, it is error-proofed by a "timeout" input of five seconds and nested within a while loop.  Thus, if the API doesn't respond within five seconds, rather than an error being raised and the program aborting, the request will continue to be made until the `CTP_daily.csv` file exists in the `root_dir` folder.

</p>
</details>

<details><summary><strong><em>get_JH_data</em></strong></summary>
<p>

This function performs a Git pull on the JH repo stored in the `JH_data` subfolder.  It uses the GitPython module to create a Git class object, giving it the `JH_data_dir` as the target folder, and using the pull() method to perform the git pull.

</p>
</details>

<details><summary><strong><em>create_JH_master</em></strong></summary>
<p>

This function creates a new `JH_master.csv` file if one does not already exist in the `root_dir`.  It loops thru all of the existing files in the `JH_data_dir` and concatenates them into a single dataframe.  This dataframe is then sorted by date and saved as `JH_master.csv` in the `root_dir` folder.

</p>
</details>

<details><summary><strong><em>update_JH_master</em></strong></summary>
<p>

This function first sets the `'Last_Update'` column in the `JH_master` dataframe to a datetime data type and drops the time portion, leaving only the date parts.

The next step is to determine the new files within the `JH_data_dir` that need to be incorporated into the `JH_master` dataframe.  This is accomplished by referencing the latest date currently existing in `JH_master` and most recent data acquired via the `get_JH_data` function.  The tricky part here is that the filenames are dated one day behind the data, thus a file titled "12-15-2020.csv" actually contains data labeled as "12-16-2020".

If the last entry in `JH_master` is dated as "12-15-2020", the previously most recent file is actually titled "12-14-2020.csv".  If the next pull is done on 12-20-2020, the new files would run from "12-15-2020.csv" to "12-19-2020.csv" (data labeled 12-16-2020 to 12-20-2020).

Once the mental gymnastics of determining the new data files is accomplished, these files are then looped through and concatenated to `JH_master`.  The data is finally saved to the `root_dir` as `JH_master.csv`.  However, if the program were run more than once in a day, no new data would exist, nothing would be concatenated, and the program simply ends.

</p>
</details>


</div> 

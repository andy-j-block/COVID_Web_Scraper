# COVID Web Scraper
<div align="justify">   


### Contents
1. [Project Intent](#intent)
2. [Data Sources](#data_sources)
3. [Setup](#setup)
4. [Helper Function Explanations](#helper_fcns)


## Project Intent  <a name="intent"></a>
This web scraping tool collects COVID data from two sources (John Hopkins Github and the COVID Tracking Project), reformats the datetime information, determines what data is new, and appends it into the master dataset.

This web scraper uses two methods for data collection: using the Selenium module and associated Chromedriver to navigate to the COVID Tracking Project website and pull daily case data from their API, and launching a git shell to pull ____ from the Johns Hopkins COVID19 data repo.

This tool was built while at Ford Motor Company for my section's technical specialist Reid.  He was keeping the team up to date on the latest COVID numbers locally and regionally through several Tableau visualizations.  Unfortunately though, the process he was using of manually collecting the data and formatting it properly was consuming a fair amount of his time, especially given that this preprocessing was a once- or twice-weekly process.  Thus, I decided to lend him a hand on this by automating the process, giving me an opportunity to practice my data scraping skills.


## Data Sources  <a name="data_sources"></a>
* COVID Tracking Project at The Atlantic - https://covidtracking.com/data/api
* Johns Hopkins COVID-19 Data Repository - https://github.com/CSSEGISandData/COVID-19


## Setup and Running  <a name="setup"></a>

This Git repo can either be downloaded as a zip or cloned onto your machine.  There is an environment YAML file in the root directory that can be used to clone the conda environment used to build this program.

The user need only run the get_COVID_data.py file in order to run the program, everything else is taken care of by the helper functions.  The get_COVID_data.py file performs the following tasks in order:

### *Initialization*
* gets the directories commonly used in the program and stores their locations as variables
* gets the Chrome and Git bash executables for use later and stores their locations as variables
* gets the current day and month and stores those as variables for later use

### *COVID Tracking Project Data*
* creates an instance of the ChromeDriver webdriver and alerts the user if there is a Chrome/ChromeDriver version mismatch
* navigates to the COVID Tracking Project's web API and downloads the daily case data
* saves the most recent data into the root directory and moves old data to the CTP_data sub-folder

### *Johns Hopkins Data*
* runs a Git pull on the data stored in the JH_data sub-folder using a subprocess and context manager
* scans the root directory for an existing instance of a JH_master CSV file
    * if none found, a new JH_master CSV file is created and populated with all the existing data up to the date of the most recent Git pull
    * if JH_master found, read in this data as a pandas dataframe and continue
* sets the 'Last_Update' column as a datetime and determines the date of the last Git pull
* takes all of the new data since the last Git pull file by file and adds their contents to the JH_master CSV
* saves the updated JH_master CSV file to the root directory

Please see the following section for a more detailed explanation of all of the helper functions. 


## Helper Function Explanations  <a name="helper_fcns"></a>

<details><summary><strong><em>get_dirs</em></strong></summary>
<p>

This function returns the locations of five directories commonly used throughout the program.  The subsequent helper files require many of these directories as inputs. The five directory outputs are as follows:

* `root_dir` - the root directory on the host machine
* `helper_files_dir` - the sub-directory containing all the helper files and modules
* `downloads_dir` - the downloads folder of the host machine
* `CTP_data_dir` - the directory where historical daily CTP reports will be moved to
* `JH_data_dir` - the sub-directory within the JH github repo where the daily reports are stored

The `downloads_dir` directory is the only directory located outside of the webscraper's repository.  Thus, it has been defaulted to the Downloads folder on Windows.  If this folder cannot be found (i.e., user running a different OS), the function will prompt the user to indentify the location of the host machine's Downloads folder.

</p>
</details>

<details><summary><strong><em>get_executables</em></strong></summary>
<p>

This function allows for easier usage of this webscraper across operating systems by identifying the locations of the Chrome browser and Git bash executables.  It returns the following two variables:

* `chrome_exe`
* `git_bash_exe`

Again, my personal computer runs Windows and thus I've set the locations of these executables to their default locations on Windows.  However, if this program is run on a non-Windows machine, a warning box will open indicating that the executables cannot be found and a file dialog box is subsequently opened in which the user can identify their locations.

</p>
</details>

<details><summary><strong><em>get_executables</em></strong></summary>
<p>

This function simply returns the day and month at the time of running the program.  They are stored as the following variables:

* `current_day`
* `current_month`

These variables are used in the get_CTP_data function for file labeling purposes.

</p>
</details>

<details><summary><strong><em>create_webdriver</em></strong></summary>
<p>

This function performs two actions:

* Aquires the version of Chrome currently installed on the host machine
* Creates an instance of the webdriver for use in get_CTP_data function

Acquiring the Chrome version is accomplished via the win32api module, pulling the requisite information from the Chrome executable's file properties.  If a Chrome/ChromeDriver version mismatch is detected in the next step, the user will be displayed the current Chrome browser version and requested to download the associated ChromeDriver version.  This check obviously cannot run on non-Windows machine so it is effectively bypassed if this is the case.

Creating an instance of the webdriver will confirm whether the correct version of ChromeDriver is available on the machine.  If not, the user will be prompted to download the correct ChromeDriver zip file.  The zip file contents are then extracted and moved to the *helper_files* directory.  The test is then run again and either passes if the user downloaded the correct ChromeDriver version or aborts after three failed attempts.  This breaks the entire program and a printed cancellation message is displayed.

</p>
</details>

<details><summary><strong><em>get_CTP_data</em></strong></summary>
<p>

This function does the hard yards of getting the COVID Tracking Project (CTP) data, formatting the filename, moving it to where it needs to be, etc.

Selenium is powering the driver functionality to navigate within the browser.  After accessing the COVID Tracking Project's website, the driver clicks its way to the link where the target data is stored.

One snag discovered during robustness testing was that sometimes the browser would timeout after requesting data from the API and the data would not be successfully downloaded.  Thus, I implemented my own timer to restart the process if the browser timeout issue occurred.

Since these files contain daily data, the last part of this function will scan the contents of the root directory for an existing daily file and move it to the CTP_data sub-folder if it exists.  It's only at this point that the just-downloaded daily file is renamed to include the `current_day` and `current_month` (from *get_todays_date* function) and moved to the root directory.

</p>
</details>

<details><summary><strong><em>get_JH_data</em></strong></summary>
<p>

This function performs a git pull on the JH repo stored in the JH_data folder.  It uses the subprocess module to open a git bash using the executable stored in `git_bash_exe`.  It also employs a context manager to take care of opening and closing the subprocess.

</p>
</details>

<details><summary><strong><em>create_JH_master</em></strong></summary>
<p>

This function creates a new JH_master CSV file if one does not already exist in the main root folder.  This will take all of the 

</p>
</details>

<details><summary><strong><em>update_JH_master</em></strong></summary>
<p>



</p>
</details>




</div> 
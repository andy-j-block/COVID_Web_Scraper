# COVID_Web_Scraper
This web scraping tool collects COVID data from two sources (John Hopkins Github and the COVID Tracking Project) , reformats the datetime information, determines what data is new, and appends it into the master dataset.

## Project Intent
This tool was built while at Ford Motor Company for my section's technical specialist Reid.  He was keeping the team up to date on the latest COVID numbers locally and regionally through several Tableau visualizations.  Unfortunately though, the process he was using of manually collecting the data and formatting it properly was consuming a fair amount of his time, especially given that this preprocessing was a once- or twice-weekly process.  Thus, I decided to lend him a hand on this by automating the process and giving me an opportunity to practice my data scraping skills.

## Data Sources
* COVID Tracking Project at the Atlantic - https://covidtracking.com/data/api
* Johns Hopkins COVID-19 Data Repository - https://github.com/CSSEGISandData/COVID-19

## Features
* VPN Check
  * Ensures that the user is connected to the Ford VPN
* Directory Check
  * Ensures the user has all the necessary helper files required to run the script and alerts the user through assert statements if a given file is missing from the base directory

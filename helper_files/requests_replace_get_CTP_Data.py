import requests
import pandas as pd


#while file does not exist:
#try:
# r = requests.get('https://api.covidtracking.com/v1/states/daily.csv', timeout=10)

# with open('daily_file.csv','wb') as f:
#     f.write(r.content)

df = pd.read_csv('daily_file.csv')
#30 Days of Python Programming
# Arewa Data Science Fellowship 
# Day 22

import requests
from bs4 import BeautifulSoup
import json
import pandas as pd

#1. 

url = 'http://www.bu.edu/president/boston-university-facts-stats/'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
text_data = []

for tag in soup.find_all(True):
    if tag.name == 'script' or tag.name == 'style':
        continue
    if tag.string:
        text_data.append(tag.string.strip())

with open('data.json', 'w') as f:
    json.dump(text_data, f)


#2.

url = 'https://archive.ics.uci.edu/ml/datasets.php'
response = requests.get(url)

dfs = pd.read_html(response.content)
table = dfs[5]

table_json = table.to_json(orient='records')

with open('table.json', 'w') as f:
    f.write(table_json)

#3. 

url = 'https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States'

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

table = soup.find_all('table')[0]

data = []
headers = []

for row in table.find_all('tr'):
    if not headers:
        headers = [cell.text.strip() for cell in row.find_all('th')]
    else:
        values = [cell.text.strip() for cell in row.find_all('td')]
        if values:
            data.append(dict(zip(headers, values)))

with open('presidents.json', 'w') as f:
    json.dump(data, f)

print('Data saved to presidents.json')

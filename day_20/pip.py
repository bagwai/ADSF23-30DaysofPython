#30 Days of Python Programming
# Arewa Data Science Fellowship 
# Day 20

import requests
import re
from collections import Counter
from nltk.corpus import stopwords
import nltk
#nltk.download('stopwords')
import statistics


#1.

# retrieve text from the URL
url = 'http://www.gutenberg.org/files/1112/1112.txt'
response = requests.get(url)
text = response.text

# clean the text
text = re.sub(r'\d+', '', text) # remove numbers
text = re.sub(r'[^\w\s]', '', text) # remove punctuation
text = text.lower() # convert all text to lowercase

# remove stop words
stop_words = set(stopwords.words('english'))
words = text.split()
filtered_words = [word for word in words if word not in stop_words]

# count the frequency of each word
word_counts = Counter(filtered_words)

# get the 10 most frequent words
most_common_words = word_counts.most_common(10)
print(most_common_words)

#2.

cats_api = 'https://api.thecatapi.com/v1/breeds'

response = requests.get(cats_api)
data = response.json()
weights = []
lifespans = []

for cat in data:
    if 'metric' in cat['weight']:
        weight = float(cat['weight']['metric'].split()[0])
        weights.append(weight)
    
    if cat['life_span'] != 'Unknown':
        lifespan = int(cat['life_span'].split()[0])
        lifespans.append(lifespan)

# Weight statistics
weight_min = min(weights)
weight_max = max(weights)
weight_mean = statistics.mean(weights)
weight_median = statistics.median(weights)
weight_stdev = statistics.stdev(weights)

# Lifespan statistics
lifespan_min = min(lifespans)
lifespan_max = max(lifespans)
lifespan_mean = statistics.mean(lifespans)
lifespan_median = statistics.median(lifespans)
lifespan_stdev = statistics.stdev(lifespans)

frequency_table = {}

for cat in data:
    if cat['origin'] not in frequency_table:
        frequency_table[cat['origin']] = {}
    
    if cat['name'] not in frequency_table[cat['origin']]:
        frequency_table[cat['origin']][cat['name']] = 0
    
    frequency_table[cat['origin']][cat['name']] += 1


#3.


# get the list of all countries from API
url = "https://restcountries.eu/rest/v2/all"
response = requests.get(url)
data = response.json()

# create a dictionary with country name and area
country_area = {country["name"]: country["area"] for country in data if country["area"] is not None}
largest_countries = sorted(country_area.items(), key=lambda x: x[1], reverse=True)[:10]

print("The 10 largest countries are:")
for country in largest_countries:
    print(country[0], "-", country[1], "sq. km")


# create a dictionary with language and population
language_population = {}
for country in data:
    for language in country["languages"]:
        if language["name"] not in language_population:
            language_population[language["name"]] = country["population"]
        else:
            language_population[language["name"]] += country["population"]

most_spoken_languages = sorted(language_population.items(), key=lambda x: x[1], reverse=True)[:10]

print("The 10 most spoken languages are:")
for language in most_spoken_languages:
    print(language[0], "-", language[1], "speakers")


# create a set to store all the languages
languages = set()
for country in data:
    for language in country["languages"]:
        languages.add(language["name"])
num_languages = len(languages)

print("The total number of languages in the countries API is:", num_languages)

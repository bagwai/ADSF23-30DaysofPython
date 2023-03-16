#30 Days of Python Programming
# Arewa Data Science Fellowship 
# Day 25

import pandas as pd

df = pd.read_csv('hacker_news.csv')

first_five_rows = df.head()
print(first_five_rows)

last_five_rows = df.tail()
print(last_five_rows)

title_series = df['title']
print(title_series)

num_rows, num_cols = df.shape
print("Number of rows:", num_rows)
print("Number of columns:", num_cols)


python_titles = df[df['title'].str.contains('Python')]
print(python_titles)

js_titles = df[df['title'].str.contains('JavaScript')]
print(js_titles)

# Look at the columns and their data types
print(df.dtypes)

# Check for missing values
print(df.isnull().sum())

# Explore the distribution of the 'score' column
import matplotlib.pyplot as plt

plt.hist(df['author'], bins=50)
plt.show()

# Look at the top 10 most frequent authors
top_authors = df['author'].value_counts().head(10)
print(top_authors)


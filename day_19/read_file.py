#30 Days of Python Programming
# Arewa Data Science Fellowship 
# Day 19

import os
import json
import re
from collections import Counter
import csv

#1. 
def count_lines_and_words(filename):
    filepath = os.path.join('data', filename)
    with open(filepath, 'r') as file:
        text = file.read()
        lines = text.splitlines()
        words = text.split()
    return len(lines), len(words)

# Obama speech
obama_lines, obama_words = count_lines_and_words('obama_speech.txt')
print(f"Obama speech has {obama_lines} lines and {obama_words} words.\n")

# Michelle Obama speech
michelle_lines, michelle_words = count_lines_and_words('michelle_obama_speech.txt')
print(f"Michelle Obama speech has {michelle_lines} lines and {michelle_words} words.\n")

# Donald Trump speech
donald_lines, donald_words = count_lines_and_words('donald_speech.txt')
print(f"Donald Trump speech has {donald_lines} lines and {donald_words} words.\n")

# Melania Trump speech
melania_lines, melania_words = count_lines_and_words('melina_trump_speech.txt')
print(f"Melania Trump speech has {melania_lines} lines and {melania_words} words.\n")

#2. 

def most_spoken_languages(filename, n):
    with open(filename, encoding='utf-8') as f:
        countries = json.load(f)
        
    languages = {}
    for country in countries:
        for language in country['languages']:
            if language in languages:
                languages[language] += 1
            else:
                languages[language] = 1

    return sorted(languages.items(), key=lambda x: x[1], reverse=True)[:n]

print(most_spoken_languages(filename='./data/countries_data.json', n=10))
print(most_spoken_languages(filename='./data/countries_data.json', n=3))


#3

def most_populated_countries(filename, n):
    with open(filename, encoding='utf-8') as f:
        countries = json.load(f)
        sorted_countries = sorted(countries, key=lambda x: x['population'], reverse=True)
        return [{'country': c['name'], 'population': c['population']} for c in sorted_countries[:n]]

print(most_populated_countries(filename='./data/countries_data.json', n=10))
print(most_populated_countries(filename='./data/countries_data.json', n=3))


#Exercises: Level 2
#4. 
with open('./data/email_exchanges_big.txt', 'r') as f:
    content = f.read()
# Use regular expressions to extract email addresses
email_regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
emails = re.findall(email_regex, content)
print(emails)

#5. 

def find_most_common_words(input_str, n):
    if isinstance(input_str, str):
        # If input_str is a string, convert it to a list of words
        words = re.findall('\w+', input_str.lower())
    else:
        # Otherwise, assume it's a file and read the file contents
        with open(input_str, 'r') as f:
            words = re.findall('\w+', f.read().lower())
    word_counts = Counter(words)
    return word_counts.most_common(n)

print(find_most_common_words('./data/sample.txt', 10))
print(find_most_common_words('./sample.txt', 5))


#6.

def find_most_frequent_words(file_path, n):
    # Read file contents
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read().lower()

    # Remove punctuation
    for char in ['.', ',', ':', ';', '!', '?', '"', '(', ')', '[', ']', '{', '}', "'s", "'"]:
        text = text.replace(char, '')
    words = text.split()
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_words[:n]


def print_top_n_words(speaker, n):
    filename = f"./data/{speaker}.txt"
    print(f"Top {n} words used by {speaker}:")
    print(find_most_frequent_words(filename, n))
    print()

# Print top 10 words for each speaker
print_top_n_words("obama_speech", 10)
print_top_n_words("michelle_obama_speech", 10)
print_top_n_words("donald_speech", 10)
print_top_n_words("melina_trump_speech", 10)


#6.

def clean_text(text):
    # Remove all non-word characters (everything except numbers and letters)
    text = re.sub(r"[^\w\s]", "", text)
    # Remove all digits
    text = re.sub(r"\d", "", text)
    # Convert to lowercase
    text = text.lower()
    return text

def remove_support_words(text):
    # Load stop words from file
    with open("./data/stop_words.py") as f:
        stop_words = f.read().splitlines()
    # Remove stop words from text
    words = text.split()
    words = [word for word in words if word not in stop_words]
    text = " ".join(words)
    return text

def check_text_similarity(text1, text2):
    # Clean and remove stop words from both texts
    text1 = remove_support_words(clean_text(text1))
    text2 = remove_support_words(clean_text(text2))
    # Calculate similarity using Jaccard index
    set1 = set(text1.split())
    set2 = set(text2.split())
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    similarity = intersection / union
    return similarity

with open("./data/michelle_obama_speech.txt") as f:
    michelle_text = f.read()

with open("./data/melina_trump_speech.txt") as f:
    melina_text = f.read()

similarity = check_text_similarity(michelle_text, melina_text)
print(f"The similarity between Michelle's speech and Melina's speech is {similarity:.2f}")


#8. 

def find_most_common_words(filename, num_words):
    with open(filename, 'r') as f:
        text = f.read()
        
    # Clean the text by removing special characters and converting to lowercase
    text = re.sub('[^A-Za-z0-9]+', ' ', text)
    text = text.lower()
    
    # Remove stop words
    with open('./data/stop_words.py', 'r') as f:
        stop_words = set(f.read().split())
    words = text.split()
    words = [w for w in words if w not in stop_words]
    
    # Count the frequency of each word
    word_counts = Counter(words)
    
    # Return the top num_words most frequent words
    return word_counts.most_common(num_words)
    
# Find the 10 most repeated words in romeo_and_juliet.txt
print(find_most_common_words('./data/romeo_and_juliet.txt', 10))


#9. 

# Open the CSV file and create a CSV reader object
with open('data/hacker_news.csv', 'r') as file:
    reader = csv.reader(file)

    # Initialize counters for each condition
    python_count = 0
    javascript_count = 0
    java_count = 0

    # Loop through each row in the CSV file
    for row in reader:
        # Convert the row to a lowercase string
        row_str = str(row).lower()

        # Check if the row contains "python" or "Python"
        if 'python' in row_str:
            python_count += 1

        # Check if the row contains "JavaScript", "javascript", or "Javascript"
        if 'javascript' in row_str:
            javascript_count += 1

        # Check if the row contains "Java" but not "JavaScript"
        if 'java' in row_str and 'javascript' not in row_str:
            java_count += 1

    # Print the results
    print(f"Number of lines containing 'python' or 'Python': {python_count}")
    print(f"Number of lines containing 'JavaScript', 'javascript', or 'Javascript': {javascript_count}")
    print(f"Number of lines containing 'Java' but not 'JavaScript': {java_count}")

#30 Days of Python Programming
# Arewa Data Science Fellowship 
# Day 17

import re
from collections import Counter

# 1. 

paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'

# Remove all the punctuations and convert the text into lowercase
cleaned_text = re.sub(r'[^\w\s]', '', paragraph).lower()
words = cleaned_text.split()

# Count the frequency of each word using dictionary
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

most_frequent_word = max(word_count, key=word_count.get)

print("The most frequent word is:", most_frequent_word)


text = "The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction."
pattern = r'-?\d+'
# r: raw string, -?: optional minus sign, \d+: one or more digits
points = list(map(int, re.findall(pattern, text)))

sorted_points = sorted(points)
furthest_distance = sorted_points[-1] - sorted_points[0]

print("The distance between the two furthest particles is:", furthest_distance)


#2. 

def is_valid_variable(variable_name):
    pattern = r'^[a-zA-Z_][a-zA-Z0-9_]*$'
    return bool(re.match(pattern, variable_name))

print(is_valid_variable('first_name'))    # True
print(is_valid_variable('first-name'))    # False
print(is_valid_variable('1first_name'))   # False
print(is_valid_variable('firstname'))     # True


#3. 
def clean_text(text):
    # Remove all special characters except for spaces
    cleaned = re.sub(r'[^\w\s]', '', text)
    # Remove all digits
    cleaned = re.sub(r'\d+', '', cleaned)
    # Remove extra spaces
    cleaned = re.sub(r'\s+', ' ', cleaned)
    # Convert to lowercase
    cleaned = cleaned.lower()
    return cleaned.strip()

sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

cleaned_text = clean_text(sentence)
print(cleaned_text)

word_counts = Counter(cleaned_text.split())
most_common = word_counts.most_common(3)
print(most_common)

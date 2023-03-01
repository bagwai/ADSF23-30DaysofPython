#30 Days of Python Programming
# Arewa Data Science Fellowship 
# Day 17

import re
from collections import Counter

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

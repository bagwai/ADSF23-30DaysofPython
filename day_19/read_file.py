#30 Days of Python Programming
# Arewa Data Science Fellowship 
# Day 19
import os

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

#30 Days of Python Programming
# Arewa Data Science Fellowship 
# Day 18

def count_lines_and_words(filename):
    # Open the file
    with open(filename, 'r') as file:
        # Read the entire file
        text = file.read()
        # Count the number of lines
        num_lines = len(text.split('\n'))
        # Count the number of words
        num_words = len(text.split())
    # Return the results
    return num_lines, num_words

# Call the function on each text file
obama_lines, obama_words = count_lines_and_words('./ADSF23-30DaysofPython/data/obama_speech.txt')
michelle_lines, michelle_words = count_lines_and_words('./ADSF23-30DaysofPython/data/michelle_obama_speech.txt')
donald_lines, donald_words = count_lines_and_words('./ADSF23-30DaysofPython/data/donald_speech.txt')
melania_lines, melania_words = count_lines_and_words('./ADSF23-30DaysofPython/data/melania_trump_speech.txt')

# Print the results
print('Obama speech:')
print('Number of lines:', obama_lines)
print('Number of words:', obama_words)

print('Michelle Obama speech:')
print('Number of lines:', michelle_lines)
print('Number of words:', michelle_words)

print('Donald Trump speech:')
print('Number of lines:', donald_lines)
print('Number of words:', donald_words)

print('Melania Trump speech:')
print('Number of lines:', melania_lines)
print('Number of words:', melania_words)

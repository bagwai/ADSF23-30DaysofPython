#30 Days of Python Programming
# Arewa Data Science Fellowship 
# Day 7
# Exercises Level 1

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]


print(len(it_companies))

# addinga Twitter to the set
it_companies.add('Twitter')
print("IT companies set after adding 'Twitter': ", it_companies)

# adding multiple IT companies to the set
it_companies.update(['Tesla', 'SpaceX', 'Alphabet'])
print("IT companies set after adding multiple companies: ", it_companies)

#5. removing an IT company from the set
it_companies.remove('IBM')
print("IT companies set after removing 'IBM': ", it_companies)

#5. using discard method to remove an IT company from the set
it_companies.discard('Tesla')
print("IT companies set after removing 'Tesla' using discard: ", it_companies)


# Exercises Level 2

# Join A and B
C = A.union(B)
print("Join A and B:", C)

# Find A intersection B
D = A.intersection(B)
print("A intersection B:", D)

# Is A subset of B
print("Is A subset of B:", A.issubset(B))

# Are A and B disjoint sets
print("Are A and B disjoint sets:", A.isdisjoint(B))

# Join A with B and B with A
E = A.union(B)
F = B.union(A)
print("Join A with B:", E)
print("Join B with A:", F)

# Symmetric difference between A and B
G = A.symmetric_difference(B)
print("Symmetric difference between A and B:", G)

# Delete the sets completely
del it_companies
del A
del B


# Exercises Level 3

age = [22, 19, 24, 25, 26, 24, 25, 24]
age_set = set(age)
print("Length of list age:", len(age))
print("Length of set age_set:", len(age_set))

# String: A string is a sequence of characters, enclosed in single or double quotes. Strings are immutable, which means once a string is created, it can't be changed.
# List: A list is a collection of items, similar to an array. Lists are mutable, which means items can be added, removed, or modified. Lists are surrounded by square brackets [].
# Tuple: A tuple is similar to a list, but it is immutable, which means once a tuple is created, its items cannot be changed. Tuples are surrounded by parentheses ().
# Set: A set is an unordered collection of unique items. Sets are mutable and do not allow duplicate elements. Sets are surrounded by curly braces {}.

sentence = "I am a teacher and I love to inspire and teach people."
words = sentence.split()
unique_words = set(words)
print("Unique words:", unique_words)
print("Number of unique words:", len(unique_words))


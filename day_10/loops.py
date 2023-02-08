import countries
import countries_data
#30 Days of Python Programming
# Arewa Data Science Fellowship 
# Day 10
# Exercises Level 1

#1. Iterate 0 to 10 using for loop, do the same using while loop.

for i in range(11):
    print(i)

i = 0
while i <= 10:
    print(i)
    i += 1

#2. Iterate 10 to 0 using for loop, do the same using while loop.
for i in range(10, -1, -1):
    print(i)

i = 10
while i >= 0:
    print(i)
    i -= 1

#3. Write a loop that makes seven calls to print(), so we get on the output the following triangle:
for i in range(1, 8):
    print("#" * i)

#4. Use nested loops to create the following

for i in range(8):
    for j in range(8):
        print("#", end=" ")
    print("")

#5. Print the following pattern:

for i in range(11):
    print(i, "x", i, "=", i*i)

#6. Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.

lst = ['Python', 'Numpy','Pandas','Django', 'Flask']
for item in lst:
    print(item)

#7. Use for loop to iterate from 0 to 100 and print only even numbers

for i in range(0, 101, 2):
    print(i)

#8. Use for loop to iterate from 0 to 100 and print only odd numbers
for i in range(1, 101, 2):
    print(i)

#Exercises Level 2

#1. Use for loop to iterate from 0 to 100 and print the sum of all numbers.

sum = 0
for i in range(101):
    sum += i
print("The sum of all numbers is", sum)

#2. Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.

even_sum = 0
odd_sum = 0
for i in range(101):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i
print("The sum of all evens is", even_sum)
print("The sum of all odds is", odd_sum)


# Exercises: Level 3
#1. Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.

land_countries = []
for country in countries.countries_lst:
    if "land" in country:
        land_countries.append(country)
print(land_countries)

#2. This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.

fruits = ['banana', 'orange', 'mango', 'lemon']

reversed_fruits = []
for fruit in fruits[::-1]:
    reversed_fruits.append(fruit)
print(reversed_fruits)

#3. Go to the data folder and use the countries_data.py file

# Total number of languages
languages = {}
for country in countries_data.countries_data:
    for language in country['languages']:
        if language not in languages:
            languages[language] = 1
        else:
            languages[language] += 1

print(f"Total number of languages: {len(languages)}")

# Ten most spoken languages
most_spoken_languages = sorted(languages.items(), key=lambda x: x[1], reverse=True)[:10]
print("Ten most spoken languages:")
for language, count in most_spoken_languages:
    print(f"{language}: {count}")

# Ten most populated countries
most_populated_countries = sorted(countries_data.countries_data, key=lambda x: x['population'], reverse=True)[:10]
print("Ten most populated countries:")
for country in most_populated_countries:
    print(f"{country['name']}: {country['population']}")


#30 Days of Python Programming
# Arewa Data Science Fellowship 
# Day 14
from functools import reduce
from countries_data import countries_data

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

"""
The difference between map, filter, and reduce:
map: is a higher-order function that takes a function and a sequence (e.g. list) as arguments and returns a new sequence with the results of applying the function to each item in the original sequence.

filter: is a higher-order function that takes a function and a sequence as arguments and returns a new sequence with only the items for which the function returns True.

reduce: is a higher-order function that takes a function and a sequence as arguments and returns a single value that is the result of applying the function to the items in the sequence.

The difference between higher order function, closure and decorator:

Higher Order Function: is a function that takes another function as an argument, returns a function as a result or both.

Closure: is a function object that remembers values in the enclosing scope even if they are not present in memory.

Decorator: is a special type of function that takes another function and extends the behavior of the latter function without explicitly modifying its source code.
"""
#Example
def square(x):
  return x * x

result = map(square, numbers)
print(result)

# 4. Use for loop to print each country in the countries list.
for country in countries:
  print(country)

#5. se for to print each name in the names list.

for name in names:
  print(name)

#6. Use for to print each number in the numbers list.

for number in numbers:
  print(number)

#Exercises: Level 2


#1. Use map to create a new list by changing each country to uppercase in the countries list
countries_uppercase = list(map(lambda x: x.upper(), countries))
print(countries_uppercase)

#2. Use map to create a new list by changing each number to its square in the numbers list
numbers_squared = list(map(lambda x: x**2, numbers))
print(numbers_squared)

#3 Use map to change each name to uppercase in the names list
names_uppercase = list(map(lambda x: x.upper(), names))
print(names_uppercase)

#4. Use filter to filter out countries containing 'land'
countries_filtered = list(filter(lambda x: 'land' in x, countries))
print(countries_filtered)

#5. Use filter to filter out countries having exactly six characters
countries_six_chars = list(filter(lambda x: len(x) == 6, countries))
print(countries_six_chars)

#6. Use filter to filter out countries containing six letters and more in the country list
countries_six_letters = list(filter(lambda x: len(x) >= 6, countries))
print(countries_six_letters)

#7. Use filter to filter out countries starting with an 'E'
countries_starts_with_E = list(filter(lambda x: x.startswith('E'), countries))
print(countries_starts_with_E)

#8. Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
result = reduce(lambda x, y: x + y, map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers)))
print(result)

#9. Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.
def get_string_lists(arr):
  return list(filter(lambda x: isinstance(x, str), arr))

#10. Use reduce to sum all the numbers in the numbers list.
sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print(sum_of_numbers)

#11. Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
sentence = reduce(lambda x, y: x + ', ' + y, countries) + ' are north European countries'
print(sentence)

#10. Declare a function called categorize_countries that returns a list of countries with some common pattern (you can find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).
def categorize_countries(countries, pattern):
  return list(filter(lambda x: x.endswith(pattern), countries))


#Exercises: Level 3
#Sort countries by name, by capital, by population
sorted_countries_by_name = sorted(countries_data, key=lambda x: x['name'])
print(sorted_countries_by_name)

sorted_countries_by_capital = sorted(countries_data, key=lambda x: x['capital'])
print(sorted_countries_by_capital)

sorted_countries_by_population = sorted(countries_data, key=lambda x: x['population'], reverse=True)
print(sorted_countries_by_population)

sorted_languages = sorted(countries_data, key=lambda x: len(x['languages']), reverse=True)
top_ten_languages = sorted_languages[:10]
print(top_ten_languages)

sorted_countries_by_population = sorted(countries_data, key=lambda x: x['population'], reverse=True)
top_ten_populated_countries = sorted_countries_by_population[:10]

print(top_ten_populated_countries)


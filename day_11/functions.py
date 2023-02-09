import math
import countries_data
#30 Days of Python Programming
# Arewa Data Science Fellowship 
# Day 11
# Exercises Level 1


#1. Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_numbers(a, b):
  return a + b

#2. Area of a circle is calculated as follows: area = π x r x r. 
def area_of_circle(radius):
  return math.pi * radius * radius

#3. Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments.
def add_all_nums(*args):
  if all(map(lambda x: type(x) == int or type(x) == float, args)):
    return sum(args)
  else:
    return "All the items in the argument list should be numbers"

#4. Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. 
def convert_celsius_to_fahrenheit(celsius):
  return (celsius * 9/5) + 32

#5. Write a function called check-season, it takes a month parameter and returns the season: 
# Autumn, Winter, Spring or Summer.
def check_season(month):
  if month in [12, 1, 2]:
    return "Winter"
  elif month in [3, 4, 5]:
    return "Spring"
  elif month in [6, 7, 8]:
    return "Summer"
  elif month in [9, 10, 11]:
    return "Autumn"
  else:
    return "Invalid month"

#6. Write a function called calculate_slope which return the slope of a linear equation
def calculate_slope(x1, y1, x2, y2):
  return (y2 - y1) / (x2 - x1)

# Exercise 7: Quadratic equation is calculated as follows: ax² + bx + c = 0. 

def solve_quadratic_eqn(a, b, c):
  discriminant = b**2 - 4*a*c
  if discriminant > 0:
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    return (root1, root2)
  elif discriminant == 0:
    root = -b / (2*a)
    return (root,)
  else:
    return "No real solutions"

#8. Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
def print_list(lst):
  for item in lst:
    print(item)

#9. Declare a function named reverse_list
def reverse_list(arr):
    reverse = []
    for i in range(len(arr)-1, -1, -1):
        reverse.append(arr[i])
    return reverse

#10. Declare a function named capitalize_list_items

def capitalize_list_items(lst):
    capitalized = []
    for item in lst:
        capitalized.append(item.capitalize())
    return capitalized

#11. Declare a function named add_item

def add_item(lst, item):
    lst.append(item)
    return lst

#12. Decleare a function named remove_item

def remove_item(lst, item):
    lst.remove(item)
    return lst

#13. Declare a function named sum_of_numbers

def sum_of_numbers(n):
    return sum(range(1, n+1))

#14. Declare a function named sum_of_odds
def sum_of_odds(n):
    return sum(i for i in range(1, n+1) if i % 2 != 0)

#15. Declare a function named sum_of_even.
def sum_of_even(n):
    return sum(i for i in range(1, n+1) if i % 2 == 0)

#Exercises: Level 2
#1. Declare a function named evens_and_odds 

def evens_and_odds(num):
    even_count = 0
    odd_count = 0
    for i in range(1, num+1):
        if i % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    print("The number of odds are {}.".format(odd_count))
    print("The number of evens are {}.".format(even_count))

#2. Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

#3. Call your function is_empty, it takes a parameter and it checks if it is empty or not

def is_empty(val):
    if val:
        return False
    else:
        return True 

#4. Write different functions which take lists
#They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).

def calculate_mean(numbers):
    return sum(numbers) / len(numbers)

def calculate_median(numbers):
    sorted_numbers = sorted(numbers)
    mid = len(numbers) // 2
    if len(numbers) % 2 == 0:
        return (sorted_numbers[mid-1] + sorted_numbers[mid]) / 2
    return sorted_numbers[mid]

def calculate_mode(numbers):
    from collections import Counter
    count = Counter(numbers)
    return max(count, key=count.get)

def calculate_range(numbers):
    return max(numbers) - min(numbers)

def calculate_variance(numbers):
    mean = calculate_mean(numbers)
    variance = 0
    for num in numbers:
        variance += (num - mean)**2
    return variance / len(numbers)

def calculate_std(numbers):
    import math
    variance = calculate_variance(numbers)
    return math.sqrt(variance)

#Exercises: Level 3
#Write a function called is_prime, which checks if a number is prime.

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def are_items_unique(lst):
    return len(lst) == len(set(lst))

def are_items_same_type(lst):
    type_ = type(lst[0])
    for item in lst:
        if type(item) != type_:
            return False
    return True

def is_valid_variable(var):
    try:
        exec(var + "= 1")
        return True
    except:
        return False

def most_spoken_languages(count, countries_data):
    # Create a dictionary to store the count of each language
    language_count = {}
    for country in countries_data:
        for language in country['languages']:
            if language in language_count:
                language_count[language] += 1
            else:
                language_count[language] = 1
    # Sort the dictionary based on the values in descending order
    sorted_languages = sorted(language_count.items(), key=lambda x: x[1], reverse=True)
    # Return the top `count` most spoken languages
    return [language[0] for language in sorted_languages[:count]]

def most_populated_countries(count, countries_data):
    # Sort the countries based on their population in descending order
    sorted_countries = sorted(countries_data, key=lambda x: x['population'], reverse=True)
    # Return the top `count` most populated countries
    return [country['name'] for country in sorted_countries[:count]]




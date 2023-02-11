#30 Days of Python Programming
# Arewa Data Science Fellowship 
# Day 13

#1. Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
neg_zero_numbers = [num for num in numbers if num <= 0]
print(neg_zero_numbers)

#2. Flatten the following list of lists of lists to a one dimensional list :

list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flattened_list = [num for sublist in list_of_lists for sub_sublist in sublist for num in sub_sublist]
print(flattened_list)

#3. Using list comprehension create the following list of tuples:

tuples = [(n, 1, n, n**2, n**3, n**4, n**5) for n in range(11)]
print(tuples)

#4. Flatten the following list to a new list:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flattened_list2 = [[country.upper(), country[:3].upper(), city.upper()] for sublist in countries for country, city in sublist]
print(flattened_list2)

#5. Change the following list to a list of dictionaries:

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
dict_list = [{'country': country.upper(), 'city': city.upper()} for sublist in countries for country, city in sublist]
print(dict_list)

#6. Change the following list of lists to a list of concatenated strings:

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
concatenated_list = [first + " " + last for sublist in names for first, last in sublist]
print(concatenated_list)

#7. Write a lambda function which can solve a slope or y-intercept of linear functions:

solve_linear_equation = lambda x1, y1, x2, y2, target: (y2-y1)/(x2-x1) if target == 'slope' else y1 - (x1 * (y2-y1)/(x2-x1)) if target == 'y-intercept' else None

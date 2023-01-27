#30 Days of Python Programming
# Arewa Data Science Fellowship 
# Day 5
# Exercises Level 1


#1-25 
empty_list = []

items_list = [8, 2, 9, 4, 5, 6, 7]
print(len(items_list))

# Get the first item, the middle item and the last item of the list
print(items_list[0])
print(items_list[len(items_list)//2])
print(items_list[-1])

# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['Mubarak', 30, '5.5ft', 'single', 'Kano, Nigeria']

# Declare a list variable named it_companies 
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies)
print(len(it_companies))
print(it_companies[0])
print(it_companies[len(it_companies)//2])
print(it_companies[-1])
it_companies[0] = 'Twitter'
print(it_companies)

# Add an IT company to it_companies
it_companies.append('Uber')

# Insert an IT company in the middle of the companies list
it_companies.insert(len(it_companies)//2, 'Spotify')

# Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[2] = it_companies[1].upper()

# Join the it_companies with a string '#;  '
print('#; '.join(it_companies))

# Check if a certain company exists in the it_companies list.
print('Uber' in it_companies)
it_companies.sort()
it_companies.reverse()
print(it_companies[:3])
print(it_companies[-3:])
print(it_companies[len(it_companies)//2-1:len(it_companies)//2+1])
it_companies.pop(0)
it_companies.pop(len(it_companies)//2-1)
it_companies.pop(-1)

# Remove all IT companies from the list
it_companies.clear()

# Destroy the IT companies list
del it_companies

#26. Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack = front_end.extend(back_end)      #using extend() method
print(full_stack)

full_stack.insert(full_stack.index('Redux') + 1, 'Python')
full_stack.insert(full_stack.index('Python') + 1, 'SQL')
print(full_stack)
#30 Days of Python Programming
# Arewa Data Science Fellowship 
# Day 8
# Exercises 

# Create an empty dictionary called dog
dog = {}

# Add name, color, breed, legs, age to the dog dictionary
dog['name'] = 'Wicked'
dog['color'] = 'black'
dog['breed'] = 'American'
dog['legs'] = 4
dog['age'] = 5

print("Dog Dictionary:", dog)

#3. Create a student dictionary
student = {}
student['first_name'] = 'Mubarak'
student['last_name'] = 'Daha'
student['gender'] = 'Male'
student['age'] = 30
student['marital_status'] = 'Single'
student['skills'] = ['Python', 'JS', 'SQL']
student['country'] = 'Nigeria'
student['city'] = 'Kano'
student['address'] = 'No 23. R/Zaki St'

print("Student Dictionary:", student)

#4. Get the length of the student dictionary
print("Length of Student Dictionary:", len(student))

#5. Get the value of skills and check the data type
skills = student['skills']
print("Skills:", skills)
print("Data type of skills:", type(skills))

#6. Modify the skills values by adding one or two skills
student['skills'].extend(['DevOps', 'R'])
print("Modified Skills:", student['skills'])

#7. Get the dictionary keys as a list
keys = list(student.keys())
print("Dictionary Keys:", keys)

#8. Get the dictionary values as a list
values = list(student.values())
print("Dictionary Values:", values)

#9. Change the dictionary to a list of tuples using items() method
items = list(student.items())
print("List of Tuples:", items)

#10. Delete one of the items in the dictionary
del student['address']
print("Dictionary after deletion:", student)

#11. Delete one of the dictionaries
del student

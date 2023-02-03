#30 Days of Python Programming
# Arewa Data Science Fellowship 
# Day 8
# Exercises Level 1

#1. Getting user input using input

my_age = 30
user_age = int(input("Enter your age: "))
if user_age >= 18:
    print("You are old enough to drive.")
else:
    years_left = 18 - user_age
    print("You need", years_left, "more years to learn to drive.")

# 2. Compare the values 
my_age = 25
user_age = int(input("Enter your age: "))
if my_age == user_age:
    print("We are the same age.")
elif my_age < user_age:
    age_difference = user_age - my_age
    if age_difference == 1:
        print("You are 1 year older than me.")
    else:
        print("You are", age_difference, "years older than me.")
else:
    age_difference = my_age - user_age
    if age_difference == 1:
        print("I am 1 year older than you.")
    else:
        print("I am", age_difference, "years older than you.")

# 3. Get two numbers from the user using input prompt.

a = int(input("Enter number one: "))
b = int(input("Enter number two: "))
if a > b:
    print(a, "is greater than", b)
elif a < b:
    print(a, "is smaller than", b)
else:
    print(a, "is equal to", b)


# Exercises: Level 2
# 1. 

score = int(input("Enter your score: "))
if score >= 80 and score <= 100:
    print("A")
elif score >= 70 and score <= 89:
    print("B")
elif score >= 60 and score <= 69:
    print("C")
elif score >= 50 and score <= 59:
    print("D")
else:
    print("F")

# 2.
month = input("Enter the month: ")
if month in ["September", "October", "November"]:
    print("Autumn")
elif month in ["December", "January", "February"]:
    print("Winter")
elif month in ["March", "April", "May"]:
    print("Spring")
elif month in ["June", "July", "August"]:
    print("Summer")

# 3.
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input("Enter a fruit: ")
if fruit in fruits:
    print("That fruit already exist in the list")
else:
    fruits.append(fruit)
    print("The modified list of fruits:", fruits)


# Exercise Level 3

person = {
    'first_name': 'Mubarak',
    'last_name': 'Daha',
    'age': 30,
    'country': 'Nigeria',
    'is_married': False,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'R/Zaki Kano',
        'zipcode': '260001'
    }
}

if 'skills' in person:
    skills = person['skills']
    middle_skill = skills[len(skills) // 2]
    print("The middle skill:", middle_skill)


if 'skills' in person:
    if 'Python' in person['skills']:
        print("The person has the Python skill")
    else:
        print("The person does not have the Python skill")


if 'skills' in person:
    skills = person['skills']
    if skills == ['JavaScript', 'React']:
        print("He is a front end developer")
    elif skills == ['Node', 'Python', 'MongoDB']:
        print("He is a backend developer")
    elif skills == ['React', 'Node', 'MongoDB']:
        print("He is a fullstack developer")
    else:
        print("unknown title")

if person['is_married'] and person['country'] == 'Finland':
    print(f"{person['first_name']} {person['last_name']} is married and lives in {person['country']}")

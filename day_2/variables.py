#Day 2: 30 Days of python programming
#Arewa Data Science Fellowship 

#Ex. Level 1. Variables decliration

first_name = "Mubarak"
last_name = "Daha Isa"
full_name = first_name + " " + last_name
country = "Nigeria"
city = "Kano"
age = 30
year = 2023
is_married = False
is_true = True
is_light_on = False
x,y,z = 2,3,4


#Ex. Level 2.1 Checking and printing the viriable type

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print((type(is_light_on)))
print(type(x))
print(type(y))
print(type(z))

#2.2 Using the len() built-in function, find the length of your first name
print(len(first_name))

#2.3 Compare the length of your first name and your last name
#Using if statement for comprehensive comparison 

if len(first_name) > len(last_name):
    print("First Name is longer")
elif len(last_name) > len(first_name):
    print("Last name is longer")
else:
    print("They have equal lengh")


#2.4 Variable operation

num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two


#2.5 Find circumference and area of a circle

radius = 30
area = 3.14 * (radius ** 2)
circumference = 2 * 3.14 * radius
print(area)
print(circumference)

#2.6 Getting input from user 

first_name = input("Enter Your First Name: ")
last_name = input("Enter Your Last Name: ")
country = input("Enter Your Country: ")
age = input("Enter Your Age: ")
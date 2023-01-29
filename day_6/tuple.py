#30 Days of Python Programming
# Arewa Data Science Fellowship 
# Day 6
# Exercises Level 1


empty_tuple = ()
brothers = ("Usman", "Sani")
sisters = ("Khadija", "Fatima")

#3. Join brothers and sisters tuples and assign it to siblings
siblings = brothers + sisters

#4. How many siblings do you have?
siblings_count = len(siblings)
print(siblings_count)

family_members = ("Father", "Mother") + siblings
print(family_members)

# Exercises Level 1

#1. Unpack siblings and parents from family_members

father, mother, *siblings = family_members

#2. Create fruits, vegetables and animal products tuples. 
fruits = ("Banana", "Orange", "Apple")
vegetables = ("Carrot", "Tomato", "Cabbage")
animal_products = ("Milk", "Egg", "Meat")
food_stuff_tp = fruits + vegetables + animal_products

#3. Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)

#4 Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
middle_items = food_stuff_tp[len(food_stuff_tp)//2 : len(food_stuff_tp)//2+1]

#5 Slice out the first three items and the last three items from food_staff_lt list
first_last_3 = food_stuff_lt[:3] + food_stuff_lt[-3:]

#6 Delete the food_staff_tp tuple completely
del food_stuff_tp

print("Apple" in food_stuff_tp) #NameError: name 'food_stuff_tp' is not defined. Did you mean: 'food_stuff_lt'?

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

# Check if 'Estonia' is a nordic country
print('Estonia' in nordic_countries)

# Check if 'Iceland' is a nordic country
print('Iceland' in nordic_countries)

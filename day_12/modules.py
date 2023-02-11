#30 Days of Python Programming
# Arewa Data Science Fellowship 
# Day 12

import random
import string

# Exercises Level 1
#1. Writ a function which generates a six digit/character random_user_id

def random_user_id():
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(6))

def user_id_gen_by_user():
    num_chars = int(input("Enter the number of characters for the user ID: "))
    num_ids = int(input("Enter the number of IDs to generate: "))
    chars = string.ascii_letters + string.digits
    return [''.join(random.choice(chars) for _ in range(num_chars)) for i in range(num_ids)]

def rgb_color_gen():
    return "rgb({}, {}, {})".format(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

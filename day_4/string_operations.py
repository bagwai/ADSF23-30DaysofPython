# Arewa Data Science Fellowship
# 30 Days Python Programming Challenge
# Day 4: String Operations 

#1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.

print("Thirty" + " " + "Days" + " " + "Of" + " " + "Python" )

#2. Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.

print("Coding" + " " + "For" + " " + "All")

#3 Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding For All"
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())
print(company[7:])
print('Coding' in company)
print(company.replace('Coding', 'Python'))
print(company.replace('Everyone', 'All'))
print(company.split())
print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(', '))
print(company[0])
print(len(company)-1)
print(company[10])

#18. Create an acronym or an abbreviation for the name 'Python For Everyone'.
sentence = 'Python For Everyone'
acronym = ''.join([word[0] for word in sentence.split()]).upper()
print(acronym)

#19. Create an acronym or an abbreviation for the name 'Coding For All'.
sentence_2 = 'Coding For All'
acronym_2 = ''.join([word[0] for word in sentence_2.split()]).upper()
print(acronym_2)

#20. 
print(company.index('C'))
print(company.index('F'))
print('Coding For All People'.rfind('l'))
print('You cannot end a sentence with because because because is a conjunction'.find('because'))
print('You cannot end a sentence with because because because is a conjunction'.rindex('because'))
print('You cannot end a sentence with because because because is a conjunction'[19:36])
print('You cannot end a sentence with because because because is a conjunction'.find('because'))
print('You cannot end a sentence with because because because is a conjunction'[19:36])
print(company.startswith('Coding'))
print(company.endswith('coding'))
print(' Coding For All '.strip())

#31. Which one of the following variables return True when we use the method isidentifier()

v1 = "30DaysOfPython"
v2 = "thirty_days_of_python"
print(v1.isidentifier()) #False
print(v2.isidentifier()) #True

#32.   
print("# ".join(['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']))


#33.
print("I am enjoying this challenge.\nI just wonder what is next.")

#34.

print("Name\tAge\tCountry\tCity")
print("Asabeneh\t250\tFinland\tHelsinki")

#35. String formatting

radius = 10
area = 3.14 * radius ** 2
print("The area of a circle with radius {} is {:.0f} meters square.".format(radius, area))

#36. String formatting

print("8 + 6 = {}".format(8 + 6))
print("8 - 6 = {}".format(8 - 6))
print("8 * 6 = {}".format(8 * 6))
print("8 / 6 = {:.2f}".format(8 / 6))
print("8 % 6 = {}".format(8 % 6))
print("8 // 6 = {}".format(8 // 6))
print("8 ** 6 = {}".format(8 ** 6))



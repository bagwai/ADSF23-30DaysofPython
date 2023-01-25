

age = 30              #age as integer
height = 53.4           #height as a float
complex_num = 3 + 4j    #complex number

#4. A script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).

base = float(input("Enter base: "))
height = float(input("Enter height: "))
area = 0.5 * base * height
print("The area of the triangle is:", area)

#5.  a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).

side_a = float(input("Enter side a: "))
side_b = float(input("Enter side b: "))
side_c = float(input("Enter side c: "))
perimeter = side_a + side_b + side_c
print("The perimeter of the triangle is:", perimeter)


#6. Calculating area of a rectangle

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area = length * width
perimeter = 2 * (length + width)
print("The area of the rectangle is:", area)
print("The perimeter of the rectangle is:", perimeter)


#7. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.

pi = 3.14
radius = float(input("Enter the radius of the circle: "))
area = pi * radius * radius
circumference = 2 * pi * radius
print("The area of the circle is:", area)
print("The circumference of the circle is:", circumference)

#8. Calculate the slope, x-intercept and y-intercept of y = 2x -2

slope = 2
x_intercept = 1
y_intercept = -2
print("The slope is:", slope)
print("The x-intercept is: (1,0)")
print("The y-intercept is: (0,-2)")


#9. Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)

x1, y1 = 2, 2
x2, y2 = 6, 10
m = (y2 - y1) / (x2 - x1)
distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
print("The slope is:", m)
print("The Euclidean distance is:", distance)

#10. Compare the slopes in tasks 8 and 9.

print("The slope in task 8 is", slope, "and the slope in task 9 is", m)
print("The slopes are equal")

#11. Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.

x = -3
y = x**2 + 6*x + 9
print("y =", y)


#12. Find the length of 'python' and 'dragon' and make a falsy comparison statement.

print(len('python') != len('dragon'))

#13. Use and operator to check if 'on' is found in both 'python' and 'dragon'

print('on' in 'python' and 'on' in 'dragon')

#14. I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.

sentence = "I hope this course is not full of jargon."
print('jargon' in sentence)

#15. There is no 'on' in both dragon and python

print('on' not in 'python' and 'on' not in 'dragon')

#16. Find the length of the text python and convert the value to float and convert it to string

x = len('python')
print(float(x))
print(str(x))

#17. Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?

num = 10
print(num % 2 == 0)

#18. Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.

print(7//3 == int(2.7))

#19. Check if type of '10' is equal to type of 10

print(type('10') == type(10))

#20. Check if int('9.8') is equal to 10

print(int("9.8") == 10) #ValueError: invalid literal for int() with base 10: '9.8'

#21. A script that prompts the user to enter hours and rate per hour. Calculate pay of the person?

hours = float(input("Enter hours: ")) # prompt the user to enter hours
rate_per_hour = float(input("Enter rate per hour: ")) # prompt the user to enter rate per hour
pay = hours * rate_per_hour     # calculate pay
print("Your weekly earning is", pay)

#22. Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years

years_lived = int(input("Enter number of years you have lived: "))
max_years = 100
total_seconds = max_years * 365 * 24 * 60 * 60
seconds_lived = years_lived * 365 * 24 * 60 * 60
print("You have lived for", seconds_lived, "seconds.")

#23. Write a Python script that displays the table

for i in range(1, 6):
    for j in range(1, 6):
        print(i ** (j-1), end=' ')
    print()


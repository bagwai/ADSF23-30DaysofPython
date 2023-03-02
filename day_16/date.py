#30 Days of Python Programming
# Arewa Data Science Fellowship 
# Day 16

from datetime import datetime


#1. Current date and time
now = datetime.now()

# Extracting date, month, year, hour, minute and timestamp
current_day = now.day
current_month = now.month
current_year = now.year
current_hour = now.hour
current_minute = now.minute
current_timestamp = datetime.timestamp(now)

print("Current date and time:", now)
print("Current day:", current_day)
print("Current month:", current_month)
print("Current year:", current_year)
print("Current hour:", current_hour)
print("Current minute:", current_minute)
print("Current timestamp:", current_timestamp)

#2. Current date and time
now = datetime.now()

# Formatting the date
formatted_date = now.strftime("%m/%d/%Y, %H:%M:%S")

print("Formatted date:", formatted_date)


#3. Time string
time_string = "5 December, 2019"

# Converting to time
time = datetime.strptime(time_string, "%d %B, %Y").time()

print("Time:", time)



#4. New year
new_year = datetime(2024, 1, 1)

# Current date and time
now = datetime.now()

# Time difference
time_difference = new_year - now

print("Time difference between now and new year:", time_difference)


#5. Epoch time
epoch = datetime(1970, 1, 1)

# Current date and time
now = datetime.now()

# Time difference
time_difference = now - epoch

print("Time difference between 1 January 1970 and now:", time_difference)


#6. Examples of using datetime module:
# The datetime module can be used for a wide range of applications, some of which include:

# Time series analysis: The datetime module can be used to manipulate and analyze time series data.

# Timestamping activities in an application: The datetime module can be used to record the timestamp of different activities in an application.

# Blogging: The datetime module can be used to add timestamps to blog posts or to schedule posts for a future date and time.

# Event scheduling: The datetime module can be used to schedule events, reminders, and appointments.

# Data analysis: The datetime module can be used to analyze data that is time-based, such as stock prices, weather data, or website traffic.
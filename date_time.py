#!/usr/local/opt/python/libexec/bin/python
# import datetime library to print date and time
from datetime import datetime, timedelta
# get current date + time
current_date = datetime.now()
# "f" is used for format.
# we need to convert datatime to string to show in output as text
output = f'Today is      : {str(current_date)}'
print(output)
# use timedelta to work with dates 
one_day = timedelta(days=1)
# lets get today's date 
# we could have re-used current_time but just for example we are getting new datetime as today
today = datetime.now()
# we can do minus to get yesterday, dates support it !!
yesterday = today - one_day
# use "f" function to format and store data in string
output = f'Yesterday was : {str(yesterday)}'
print(output)

# We can slice and dice data e.g. 
print('Day : ' + str(current_date.day))
print('Month : ' + str(current_date.month))
print('Year : ' + str(current_date.year))

# store dates with input and format
birthday = input('When is your birthday (dd/mm/yyy)? ')
# Store time with format with the help of "strptime" function
birthday_date = datetime.strptime(birthday, '%d/%m/%Y')
# print('Birthday ' + str(birthday_date))
output = f'Birthday {str(birthday_date)}'
print(output)

# to get the current date and time imports the datetime and timedelta libraries
from datetime import datetime, timedelta

today = datetime.now()
#the now function returns current date and time as a datetime object

# The now function returns current date and time as a datetime object
# before you can concatenate it to another string
print('Today is ' + str(today))

# you can use timedelta to add or remove days, or weeks to a date
one_day = timedelta(days=1)
one_week = timedelta(weeks=1)
last_week = today - one_week
yesterday = today - one_day
print('Yesterday was ' + str(yesterday))
print('Last week was ' + str(last_week))

print('Day: ' + str(today.day))
print('Month: ' + str(today.month))
print('Year: ' + str(today.year))

birthday = input('When is your birthday (dd/mm/yyyy)?: ')
birthday_date = datetime.strptime(birthday, '%d/%m/%Y')
print('Birthday: ' + str(birthday_date))
# import the lib
import datetime

# store a string representation of a date
my_date = "2017-11-13 10:22:54.677"

# parse the string into a date
date = datetime.datetime.strptime(my_date, '%Y-%m-%d %H:%M:%S.%f')

print("Date:%s" % date)
print("Day: %s" % date.day)
print("Month: %s" % date.month)
print("Year: %s" % date.year)
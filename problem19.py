#You are given the following information, but you may prefer to do some research for yourself.
#
# 1 Jan 1900 was a Monday.
#
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# 
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

# I'm thinking of the days encoded as Z mod 7 as follows:
# 0	sunday
# 1	monday
# 2 	tuesday
# 3	wednesday
# 4	thursday
# 5 	friday
# 6 	saturday

def get_day(date, month, year):
  day = 0 # We're starting with the fact that get_day(1,1,1900) = 1. We'll get 0 from the year 1900, 0 from the month january, and 1 from the date the 1st. 
  # Year
  day = (day + (year-1900)+(year-1900)//4)%7 	# 365%7=1, so we add 1 for every year since 1900. Every 4 years has a leap day, and by subtracting 1900 we conveniently leave out 1900 (which is not a leap year). 
  # Month
  if month > 1:
    day += 31
  if month > 2:
    day += 28 
    if year%4 == 0:
      day += 1 #then it's a leap year
    if year%100 == 0:
      day -= 1 #actually is isn't
    if year%400 == 0:
      day += 1 #actually it is
  if month > 3:
    day += 31
  if month > 4:
    day += 30
  if month > 5:
    day += 31
  if month > 6:
    day += 30
  if month > 7:
    day += 31
  if month > 8:
    day += 31
  if month > 9:
    day += 30
  if month > 10:
    day += 31
  if month > 11:
    day += 30
  # Day
  day = (day + date) % 7
  return day

# Now we count sundays which fall on the 1st:

count=0

for iyear in range(1900, 2001):
  for imonth in range(1,13):
    count += 1 if get_day(1,imonth,iyear) == 0 else 0
    if get_day(1,imonth,iyear) == 0:
      print("1-" + str(imonth) + "-" + str(iyear))

print(count)

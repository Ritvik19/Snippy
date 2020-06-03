# Current date and time in different formats

from datetime import datetime
d = datetime.now() #today's datetime
d
# datetime.datetime(2019, 12, 22, 13, 14, 18, 193898)

print(d.weekday()) #day of week - Monday is 0 and Sunday is 6
print(d.year)
print(d.month)
print(d.day)
print(d.hour)
print(d.minute)
print(d.second)

Date to string
print(d.strftime("%A %d/%m/%Y"))
# Sunday 22/12/2019

# String to date conversion

date_string = '2016-02-01 12:00PM'
print(datetime.strptime(date_string, '%Y-%m-%d %I:%M%p'))
# 2016-02-01 12:00:00

date_string = '02/01/2016'
d2 = datetime.strptime(date_string, '%m/%d/%Y')
print(d2)
# 2016-02-01 00:00:00

# Difference in datetime calculation

from datetime import timedelta
d = datetime.now()
date_string = '2/01/2016'
d2 = datetime.strptime(date_string, '%m/%d/%Y')
print(d - d2)

# 1420 days, 13:18:27.386763

date_diff = (d - d2)/timedelta(days=1)
print('date_diff = {} days'.format(date_diff))
# date_diff = 1420.5544836430902 days

date_diff = (d - d2)/timedelta(weeks=1)
print('date_diff = {} weeks'.format(date_diff))
# date_diff = 202.93635480615575 weeks

date_diff = (d - d2)/timedelta(days=365)
print('date_diff = {} years'.format(date_diff))
# date_diff = 3.8919300921728497 years

# Datetime plus/minus a certain period of time
print(d + timedelta(seconds=1)) # today + one second
print(d + timedelta(minutes=1)) # today + one minute
print(d + timedelta(hours=1)) # today + one hour
print(d + timedelta(days=1)) # today + one day
print(d + timedelta(weeks=1)) # today + one week
print(d + timedelta(days=1)*365) # today + one year
# 2019-12-22 13:18:28.386763
# 2019-12-22 13:19:27.386763
# 2019-12-22 14:18:27.386763
# 2019-12-23 13:18:27.386763
# 2019-12-29 13:18:27.386763
# 2020-12-21 13:18:27.386763
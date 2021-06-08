#===============#
# 1.Time Delta  #
#===============#

from datetime import datetime
from datetime import timedelta

a = timedelta(days=2, hours=6)
b = timedelta(hours=4.5)
c = a+b
print(c)
# ---> Output: 2 days, 10: 30: 00


# print days in c
print(c.days)
# ---> Output: 2

# print hours in c
print(c.seconds/3600)
# ---> Output: 10.5

# print total hours
print(c.total_seconds()/3600)
# ---> output: 58.5

#==============#
#  2.Datetime  #
#==============#

# import date time from datetime

a = datetime(2012, 9, 23)
print(a+timedelta(days=10))
# ---> Output: 2012-10-03 00:00:00


b = datetime(2021, 6, 12)
d = b-a
print(d)
# ---> Output: 3184 days, 0: 00: 00


now = datetime.today()
print(now)


# time after 10 min
after_ten_min = now+timedelta(minutes=10)
print(after_ten_min)

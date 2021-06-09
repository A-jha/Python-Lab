"""
Looping over the dates doesn’t require building a list of all the dates ahead of time. You
can just calculate the starting and stopping date in the range, then use datetime.time
delta objects to increment the date as you go.
"""
from datetime import datetime, date, timedelta
import calendar


def get_month_range(start_date=None):
    if start_date is None:
        start_date = date.today().replace(day=1)

    _, day_in_month = calendar.monthrange(start_date.year, start_date.month)
    end_date = start_date + timedelta(days=day_in_month)
    return (start_date, end_date)


a_day = timedelta(days=1)
first_day, last_day = get_month_range()
while first_day < last_day:
    print(first_day)
    first_day += a_day
"""
2021-06-01
2021-06-02
2021-06-03
2021-06-04
2021-06-05
2021-06-06
2021-06-07
2021-06-08
2021-06-09
2021-06-10
2021-06-11
2021-06-12
2021-06-13
2021-06-14
2021-06-15
2021-06-16
2021-06-17
2021-06-18
2021-06-19
2021-06-20
2021-06-21
2021-06-22
2021-06-23
2021-06-24
2021-06-25
2021-06-26
2021-06-27
2021-06-28
2021-06-29
2021-06-30
"""

# print day between range of given date


def date_range(start, stop, step):
    while start < stop:
        yield start
        start += step


for d in date_range(datetime(2021, 9, 1), datetime(2021, 9, 5), timedelta(hours=6)):
    print(d)
"""
2021-09-01 00:00:00
2021-09-01 06:00:00
2021-09-01 12:00:00
2021-09-01 18:00:00
2021-09-02 00:00:00
2021-09-02 06:00:00
2021-09-02 12:00:00
2021-09-02 18:00:00
2021-09-03 00:00:00
2021-09-03 06:00:00
2021-09-03 12:00:00
2021-09-03 18:00:00
2021-09-04 00:00:00
2021-09-04 06:00:00
2021-09-04 12:00:00
2021-09-04 18:00:00
"""

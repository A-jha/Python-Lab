from datetime import datetime
from datetime import datetime, timedelta

weekdays = ['monday', 'tuesday', 'wednesday',
            'thursday', 'friday', 'saturday', 'sunday']


def getPrevious_byDay(dayname, start_date=None):
    if start_date is None:
        start_date = datetime.today()
    day_num = start_date.weekday()
    day_num_target = weekdays.index(dayname)
    days_ago = (7 + day_num - day_num_target) % 7
    if days_ago == 0:
        days_ago = 7
    target_date = start_date - timedelta(days=days_ago)
    return target_date


today = datetime.today()
print(today)
# ---> 2021-06-09 20:48:51.212291
prev_monday_date = getPrevious_byDay('monday')
print(prev_monday_date)
# ---> 2021-06-07 20: 49: 41.197876
print(getPrevious_byDay('wednesday'))
# ---> 2021-06-02 20:51:09.433183

#============================================#
#   Relativedelta function from defaultutil  #
#============================================#

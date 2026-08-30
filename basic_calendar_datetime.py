import calendar
import datetime

# print calendar
cal = calendar.month(2026,9)
print(cal)

# print current Date & Time
date_today = datetime.date.today()
c_time = datetime.datetime.now().time()

print("Today Date: ", date_today)
print("Current Time: ", c_time)
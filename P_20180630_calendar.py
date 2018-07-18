import calendar

c_1=calendar.weekday(2018,6,30)
print(c_1)

c_2=calendar.prmonth(2018,6)
print(c_2)

print(calendar.isleap(2018))

#该月第一天是星期几，共有多少天，星期一-星期天：0-6
print(calendar.monthrange(2018,6))

print(calendar.monthcalendar(2018,6))

print(calendar.month(2018,6))

print(calendar.leapdays(1990,2018))

print(calendar.calendar(2018))
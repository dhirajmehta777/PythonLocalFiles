import calendar
print(calendar.TextCalendar(firstweekday=6).formatyear(2022))
print(calendar.weekday(2022,12,28))
print(calendar.day_name[calendar.weekday(2022,12,28)])
print(calendar.day_name[calendar.weekday(2022,12,28)].upper())
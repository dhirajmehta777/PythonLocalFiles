import datetime

current_date=datetime.datetime.today().date()
print(current_date)
print("#########################################")
current_time=datetime.datetime.today().time()
print(current_time)
print("#########################################")
current_datetime=datetime.datetime.today()
print(current_datetime)
print("#########################################")
format_datetime=current_datetime.strftime('%Y-%m-%d-%H-%M-%S-%f')
print(format_datetime)#using strftime we can format the date time as we want.
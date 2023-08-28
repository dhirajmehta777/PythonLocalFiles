day=int(input("enter day:"))
month=int(input("enter month:"))
year=int(input("enter year:"))
if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
    max_days=31
elif month==4 or month==6 or month==9 or month==11:
    max_days=30
elif year%4==0 and year%100!=0 or year%400==0:
    max_days=29
else:
    max_days=28

if month<1 or month>12:
    print("entered date is invalid")
    print("check the range of month")
elif day<1 or day>max_days:
    print("entered date is invalid")
    print("check the range of month")
elif year<1900 or year>2023:
    print("entered date is invalid")
    print("check the range of month")
else:
    print("entered date is valid")
    dd=str(day)
    mm=str(month)
    yyyy=str(year)
    if month<10:
        mm="0"+mm
    if day<10:
        dd="0"+dd
    given_date=dd+mm+yyyy
    reversed_date = given_date[::-1]
    if given_date == reversed_date:
        print("date is palindrome")
    else:
        print("date is not palindrome")
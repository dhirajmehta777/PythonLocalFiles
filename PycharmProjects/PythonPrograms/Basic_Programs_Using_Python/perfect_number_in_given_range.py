lower=int(input("enter the lower limit:"))
upper=int(input("enter the upper limit:"))
for num in range(lower,upper+1):
    result=0
    for i in range(1,num):
        if num%i==0:
            result=result+i
    if result==num:
        print(num,"is a perfect number")



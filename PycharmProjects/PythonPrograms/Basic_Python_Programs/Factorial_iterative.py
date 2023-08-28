num=5
fact=1
if num<0:
    print("The factorial does not exits for negative numbers")
elif num==0:
    print("the factorial of 0 is 1")
else:
    for i in range(1,num+1):
        fact=fact * i
    print("the factorial of",num,"is:", fact)
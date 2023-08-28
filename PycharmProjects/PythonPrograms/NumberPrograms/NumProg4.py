#check given number is special or not:59=5+9+5*9
n=int(input("Enter the number:\n"))
m=n
sum=0
prod=1
while m!=0:
    d=m%10
    sum=sum+d
    prod=prod*d
    total_sum=sum+prod
    m=m//10
if total_sum==n:
    print("Number is special")
else:
    print("Number is not a special")
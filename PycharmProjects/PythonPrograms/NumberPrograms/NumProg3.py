#check given number is spy or not:123,1+2+3=1*2*3
n=int(input("Enter the number:\n"))
m=n
sum=0
prod=1
while m!=0:
    d=m%10
    sum=sum+d
    prod=prod*d
    m=m//10
if sum==prod:
    print("Number is spy")
else:
    print("Number is not a spy")
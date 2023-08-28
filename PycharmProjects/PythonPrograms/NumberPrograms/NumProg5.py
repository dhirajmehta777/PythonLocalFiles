#check given number is Harshad/Niven or not:156=1+5+6=12, 156%12==0
n=int(input("Enter the number:\n"))
m=n
sum=0
while m!=0:
    d=m%10
    sum=sum+d
    m=m//10
if m%sum==0:
    print("Number is Niven")
else:
    print("Number is not a Niven")
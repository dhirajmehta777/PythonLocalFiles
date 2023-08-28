#check given number is palindrome or not
n=int(input("Enter the number:\n"))
m=n
sum=0
while m!=0:
    d=m%10
    sum=sum*10+d
    m=m//10
if sum==n:
    print("Number is palindrome")
else:
    print("Number is not a palindrome")
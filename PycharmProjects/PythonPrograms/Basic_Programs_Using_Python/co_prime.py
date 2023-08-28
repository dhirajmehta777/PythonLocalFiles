import math
num1=int(input("number1:"))
num2=int(input("number2:"))
if math.gcd(num1,num2)==1:
    print(num1,"and",num2,"are coprime")
else:
    print(num1,"and",num2,"are not coprime")
    
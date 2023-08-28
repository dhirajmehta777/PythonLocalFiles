import math
print(math.gcd(4,18))#Greatest common divisor of two numbers

def computegcd(a,b):
    if b==0:
        return a
    else:
        return computegcd(b,a%b)
num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
print(computegcd(num1,num2))
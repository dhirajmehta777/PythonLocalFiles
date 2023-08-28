import math
num1=int(input("number1:"))
lower=int(input("lower limit:"))
upper=int(input("upper limit:"))

for i in range(lower,upper+1):
    if math.gcd(num1,i)==1:
        print(i)


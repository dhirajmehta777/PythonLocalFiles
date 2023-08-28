import re

n=int(input("Enter the number:"))

p='^[+-]?[0-9]*\.[0-9]+$'
for i in range(n):
    s=input()
    print(bool(re.match(p,s)))
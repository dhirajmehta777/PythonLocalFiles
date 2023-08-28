# num=int(input("enter a positive integer number:"))
# result=0
# while num>0:
#     digit=num%10
#     result=result+digit
#     num=num//10
# print("sum of the digits is:",result)

"""
using for loop:
"""
num=int(input("enter a positive integer number:"))
result=0
for i in range(len(str(num))):
    digit=num%10
    result=result+digit
    num=num//10
print("sum of the digits is:",result)
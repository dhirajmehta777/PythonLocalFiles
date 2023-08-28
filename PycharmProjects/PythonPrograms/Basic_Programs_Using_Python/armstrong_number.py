#its a number which is sum of the nth power of its digits:
"""
Ex:134
here no of digits=3
Armstrong No=1^3+3^3+4^3 should be equal to the original number
"""
"""
find out the armstrong numbers in the range of 1 to 1000
"""
for i in range(1001):
    num=i
    result=0
    n=len(str(i))
    while(i!=0):
        digit=i%10
        result=result+digit**n
        i=i//10
    if num==result:
        print(num)
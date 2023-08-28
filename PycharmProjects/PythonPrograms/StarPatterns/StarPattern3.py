#Decreasing Triangle Pattern:
"""
* * * * *
* * * *
* * *
* * 
*
Here outer loop is set to n and nested loop is set to i,n
"""
n=5
for i in range(n):
    for j in range(i,n):
        print('*',end=' ')
    print()
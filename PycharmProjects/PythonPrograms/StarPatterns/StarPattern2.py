#Increasing Triangle Pattern:
"""
*
* *
* * *
* * * *
* * * * *
Here outer loop is set to n and nested loop is set to i+1
"""
n=5
for i in range(n):
    for j in range(i+1):
        print('*',end=' ')
    print()
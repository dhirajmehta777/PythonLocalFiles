"""
NumberPattern1:
1
1 1
1 1 1
1 1 1 1
1 1 1 1 1 
"""
n=5
for i in range(n):
    for j in range(i+1):
        print('1',end=' ')
    print()
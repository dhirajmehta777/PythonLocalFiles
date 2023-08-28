"""
NumberPattern5:
1
2 2
1 1 1
2 2 2 2
1 1 1 1 1 
"""
n=5
p=0
for i in range(n):
    for j in range(i+1):
        if(i%2==0):
            print('1',end=' ')
        else:
            print('2',end=' ')
    print()
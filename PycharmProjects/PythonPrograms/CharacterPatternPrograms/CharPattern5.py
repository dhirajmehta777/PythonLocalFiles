"""
CharPattern5:
A
B B
A A A
B B B B
A A A A A 
"""
n=5
for i in range(n):
    for j in range(i+1):
        if(i%2==0):
            print('A',end=' ')
        else:
            print('B',end=' ')
    print()
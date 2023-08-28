"""
NumberPattern11:
5
5 4
5 4 3
5 4 3 2
5 4 3 2 1
"""
n=5
for i in range(n):
    p=5
    for j in range(i+1):
        print(p,end=' ')
        p-=1
    print()
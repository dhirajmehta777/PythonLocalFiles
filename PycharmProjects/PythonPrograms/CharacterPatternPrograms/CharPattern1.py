"""
CharPattern1:
A
A A
A A A
A A A A
A A A A A
"""
n=5
for i in range(n):
    for j in range(i+1):
        print('A',end=' ')
    print()
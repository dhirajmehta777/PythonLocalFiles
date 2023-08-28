"""
CharPattern3:
E
D D
C C C
B B B B
A A A A A
"""
n=5
p=69
for i in range(n):
    for j in range(i+1):
        print(chr(p),end=' ')
    p-=1
    print()
"""
CharPattern14:
R
E E
D D D
O O O O
C C C C C
"""
s="CODER"
n=len(s)
p=n-1
for i in range(n):
    for j in range(i+1):
        print(s[p],end=' ')
    p-=1
    print()
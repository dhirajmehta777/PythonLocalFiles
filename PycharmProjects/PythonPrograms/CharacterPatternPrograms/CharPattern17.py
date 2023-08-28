"""
CharPattern17:
R
R E
R E D
R E D O
R E D O C
"""
s="CODER"
n=len(s)
for i in range(n):
    p = n-1
    for j in range(i+1):
        print(s[p],end=' ')
        p-=1
    print()
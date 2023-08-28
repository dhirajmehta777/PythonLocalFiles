"""
CharPattern14:
C
O O
D D D
E E E E
R R R R R 
"""
s="CODER"
n=len(s)
p=0
for i in range(n):
    for j in range(i+1):
        print(s[p],end=' ')
    p+=1
    print()
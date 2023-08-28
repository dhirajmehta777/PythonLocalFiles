"""
CharPattern4:
A
C C
E E E
G G G G
I I I I I 
"""
n=5
p=65
for i in range(n):
    for j in range(i+1):
        print(chr(p),end=' ')
    p+=2
    print()
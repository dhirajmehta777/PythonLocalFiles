"""
CharPattern9:
A
A B
A B C
A B C D
A B C D E
"""
n=5
for i in range(n):
    p=65
    for j in range(i+1):
        print(chr(p),end=' ')
        p+=1
    print()
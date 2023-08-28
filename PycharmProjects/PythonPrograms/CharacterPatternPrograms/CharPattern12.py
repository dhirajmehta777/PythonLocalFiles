"""
CharPattern12:
E
E D
E D C
E D C B
E D C B A

"""
n=5
for i in range(n):
    p=69
    for j in range(i+1):
        print(chr(p),end=' ')
        p-=1
    print()
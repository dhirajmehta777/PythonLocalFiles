"""
CharPattern6:
         A
        B B B
      C C C C C
    D D D D D D D
  E E E E E E E E E
    F F F F F F F
      G G G G G
        H H H
          I 
"""
n=5
p=65
for i in range(n-1):
    for j in range(i,n):
        print(' ',end=' ')
    for j in range(i):
        print(chr(p),end=' ')
    for j in range(i+1):
        print(chr(p),end=' ')
    p+=1
    print()
for i in range(n):
    for j in range(i+1):
        print(' ',end=' ')
    for j in range(i,n-1):
        print(chr(p),end=' ')
    for j in range(i,n):
        print(chr(p),end=' ')
    p+=1
    print()

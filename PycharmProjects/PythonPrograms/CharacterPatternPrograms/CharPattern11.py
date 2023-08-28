#NumberPattern10:
"""
          A
        A B C
      A B C D E
    A B C D E F G
  A B C D E F G H I 
"""
n=5
for i in range(n):
    p=65
    for j in range(i,n):
        print(' ',end=' ')
    for j in range(i):
        print(chr(p),end=' ')
        p+=1
    for j in range(i+1):
        print(chr(p),end=' ')
        p+=1
    print()
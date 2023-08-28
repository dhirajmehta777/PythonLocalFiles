
"""
 #CharPattern10:
  A B C D E
    A B C D
      A B C
        A B
          A
"""
n=5
for i in range(n):
    p=65
    for j in range(i+1):
        print(' ',end=' ')
    for j in range(i,n):
        print(chr(p),end=' ')
        p+=1
    print()
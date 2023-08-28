"""
CharPattern13:
  E D C B A
    D C B A
      C B A 
        B A
          A
"""
n=5
k=69
for i in range(n):
    p=k
    for j in range(i+1):
        print(' ',end=' ')
    for j in range(i,n):
        print(chr(p),end=' ')
        p-=1
    k-=1
    print()
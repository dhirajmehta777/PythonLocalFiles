"""
NumberPattern12:
  5 4 3 2 1
    4 3 2 1
      3 2 1
        2 1
          1 
"""
n=5
k=5
for i in range(n):
    p=k
    for j in range(i+1):
        print(' ',end=' ')
    for j in range(i,n):
        print(p,end=' ')
        p-=1
    k-=1
    print()
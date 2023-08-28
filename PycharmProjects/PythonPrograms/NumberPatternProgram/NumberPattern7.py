"""
NumberPattern7:
          1
        2 2 2
      3 3 3 3 3
    4 4 4 4 4 4 4
  5 5 5 5 5 5 5 5 5
    4 4 4 4 4 4 4
      3 3 3 3 3
        2 2 2
          1
"""
n=5
p=1
for i in range(n-1):
    for j in range(i,n):
        print(' ',end=' ')
    for j in range(i):
        print(p,end=' ')
    for j in range(i+1):
        print(p,end=' ')
    p+=1
    print()
p=5
for i in range(n):
    for j in range(i+1):
        print(' ',end=' ')
    for j in range(i,n-1):
        print(p,end=' ')
    for j in range(i,n):
        print(p,end=' ')
    p-=1
    print()

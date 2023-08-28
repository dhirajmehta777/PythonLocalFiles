#NumberPattern10:
"""
          1
        1 2 3
      1 2 3 4 5
    1 2 3 4 5 6 7
  1 2 3 4 5 6 7 8 9 
"""
n=5
for i in range(n):
    p=1
    for j in range(i,n):
        print(' ',end=' ')
    for j in range(i):
        print(p,end=' ')
        p+=1
    for j in range(i+1):
        print(p,end=' ')
        p+=1
    print()
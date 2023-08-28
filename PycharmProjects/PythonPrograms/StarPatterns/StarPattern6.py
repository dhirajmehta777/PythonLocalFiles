#Hill Pattern:
"""
          *
        * * *
      * * * * *
    * * * * * * *
  * * * * * * * * *
here decreasing triangle with space and followed by two increasing triangle with *
"""
n=5
for i in range(n):
    for j in range(i,n):
        print(' ',end=' ')
    for j in range(i):
        print('*',end=' ')
    for j in range(i+1):
        print('*',end=' ')
    print()
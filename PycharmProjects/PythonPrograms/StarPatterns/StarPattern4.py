#Right Sided Triangle Pattern:
"""
          *
        * *
      * * *
    * * * *
  * * * * *
here decreasing triangle with space and followed by increasing triangle with *
"""
n=5
for i in range(n):
    for j in range(i,n):
        print(' ',end=' ')
    for j in range(i+1):
        print('*',end=' ')
    print()
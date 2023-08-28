"""
NumberPattern8:
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5 
"""
n=5

for i in range(n):
    p=1
    for j in range(i+1):
        print(p,end=' ')
        p+=1
    print()
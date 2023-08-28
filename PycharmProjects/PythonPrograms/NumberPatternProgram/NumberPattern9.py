"""
NumberPattern9:
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1 
"""
n=5

for i in range(n):
    p=1
    for j in range(i,n):
        print(p,end=' ')
        p+=1
    print()
from itertools import combinations
s=input().split()
string=sorted(s[0])
num=int(s[1])
for i in range(1,num+1):
    x=list(combinations(string, i))
    for val in x:
        print(''.join(val))

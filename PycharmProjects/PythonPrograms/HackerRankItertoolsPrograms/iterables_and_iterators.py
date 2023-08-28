from itertools import combinations
n=int(input())
l=list(input().split())
k=int(input())
c=list(combinations(l,k))
x=[i for i in c if 'a' in i]
print(len(x)/len(c))
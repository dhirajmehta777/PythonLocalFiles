# n=int(input())
# d=dict()
# for i in range(1,n+1):
#     v=input()
#     if v in d:
#         d[v].append(i)
#     else:
#         d[v]=[i]
# print(d.items())
# for key,val in d.items():
#     print(key,val)
###################################################
# from collections import defaultdict
# d=defaultdict(list)
# n=int(input())
# for i in range(1,n+1):
#     v=input()
#     d[v].append(i)
# print(d.items())
# for key,val in d.items():
#     print(key,val)
###################################################
from collections import defaultdict
d=defaultdict(list)
n,m=map(int, input().split())

for i in range(1,n+1):
    v=input()
    d[v].append(i)

for i in range(m):
    k=input()
    if k in d:
        print(*d[k],sep=" ")
    else:
        print(-1)
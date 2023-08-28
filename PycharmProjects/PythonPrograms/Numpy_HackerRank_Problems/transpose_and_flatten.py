import numpy as np

# nm=input().split()
# n,m=int(nm[0]), int(nm[1])
# l=[input().split() for i in range(n)]
# arr=np.array(l,dtype=int)
# print(np.transpose(arr))
# print(arr.flatten())

n,m=map(int, input().split())
list1=[]
for i in range(n):
    a=list(map(int, input().split()))
    list1.append(a)
arr=np.array(list1)
print(np.transpose(arr))
print(arr.flatten())

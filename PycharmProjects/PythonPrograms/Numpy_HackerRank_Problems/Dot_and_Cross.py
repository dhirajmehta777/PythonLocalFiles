import numpy as np
N=int(input())
a=[]
for i in range(N):
    a.append(list(map(int, input().split())))
arr1=np.array(a)
b=[]
for i in range(N):
    b.append(list(map(int, input().split())))
arr2=np.array(b)


print (np.dot(arr1, arr2) )
# n=int(input())
# name=input().split()
# lis=[]
# s=0
# for i in range(n):
#     lis.append(input().split())
# k=name.index("MARKS")
# for i in range(n):
#     s+=int(lis[i][k])
# print(s/n)

#using namedtuple
# from collections import namedtuple
# Car=namedtuple('car','price milage colour classes')
# xyz=Car(price=1000000, milage=30, colour='cyan', classes='y')
# print(xyz)
# print(xyz.colour)

from collections import namedtuple
n=int(input())
student=namedtuple('student',input())
lst=[]
s=0
for i in range(n):
    x=input().split()
    s1=student(*x)
    lst.append(s1)
for i in range(n):
    s+=int(lst[i].MARKS)

print(s/n)
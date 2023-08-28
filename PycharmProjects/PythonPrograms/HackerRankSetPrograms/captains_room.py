K=int(input())
rooms=list(map(int, input().split()))
# actual_rooms=list(set(rooms))*K
# difference=sum(actual_rooms)-sum(rooms)
# print(int(difference/(K-1)))

set1=set()
set2=set()
for i in rooms:
    if i in set1:
        set2.add(i)
    else:
        set1.add(i)
s=set1.difference(set2)
print(*s)

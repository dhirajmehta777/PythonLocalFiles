n = int(input())
s = set(map(int, input().split()))
m=int(input())
for i in range(m):
    s1=list(input().split())
    if s1[0]=="pop":
        s.pop()
    elif s1[0]=="remove":
        s.remove(int(s1[1]))
    elif s1[0]=="discard":
        s.discard(int(s1[1]))
sum=0
for i in s:
    sum=sum+i
print(sum)
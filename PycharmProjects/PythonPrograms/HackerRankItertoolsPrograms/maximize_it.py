from itertools import product
k,m=list(map(int,input().split()))
lines=[]

for item in range(k):
    lines.append(list(map(int, input().split()))[1:])

result_lists=list(product(*lines))

result=[]
for tup in result_lists:
    total=0
    for item in tup:
        total=total+(item**2)
    result.append(total%m)

print(max(result))
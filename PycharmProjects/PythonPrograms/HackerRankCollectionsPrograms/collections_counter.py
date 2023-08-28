from collections import Counter
n=int(input())
stock=list(map(int, input().split()))
Dict=Counter(stock)
x=int(input())
p=0
for i in range(x):
    size, price=map(int, input().split())
    if Dict[size]:
        Dict[size]-=1
        p=p+price
print(p)
a, set_a=int(input()), set(map(int, input().split()))
N=int(input())

for i in range(0, N):
    op=input().split()
    set_b=set(map(int, input().split()))
    if op[0]=='intersection_update':
        set_a.intersection_update(set_b)
    elif op[0]=='symmetric_difference_update':
        set_a.symmetric_difference_update(set_b)
    elif op[0]=='difference_update':
        set_a.difference_update(set_b)
    elif op[0]=='update':
        set_a.update(set_b)
print(sum(set_a))
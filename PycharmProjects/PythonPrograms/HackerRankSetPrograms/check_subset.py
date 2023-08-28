T=int(input())
temp=0
for i in range(0, T):
    temp=0
    a, set_a=int(input()), set(map(int, input().split()))
    b, set_b=int(input()), set(map(int, input().split()))
    for i in set_a:
        if i in set_b:
            temp=temp+1
            continue
        else:
            print("False")
            break
    if temp==a:
        print("True")
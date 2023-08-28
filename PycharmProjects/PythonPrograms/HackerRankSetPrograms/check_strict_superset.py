A = set(map(int,input().split()))
sets = int(input())
check = 0
for x in range(sets):
    other_sets = set(map(int,input().split()))
    if other_sets.issubset(A) and len(A)>len(other_sets):
        check +=1
    else:
        check +=0
if check == sets:
    print(True)
else:
    print(False)
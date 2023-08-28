nx = list(map(int, input().split()))
n, x = nx[0], nx[1]
z = []
for i in range(x):
    z.append(list(map(float, input().split())))

v = zip(*z)
for i in v:
    print(sum(i) / x)

#int(input()) only accepts integer values but were as eval(input()) will accepts all the values like
#int, float, string, list, tuple
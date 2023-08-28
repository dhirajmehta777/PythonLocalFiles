import cmath
c=complex(input().strip())
for i in cmath.polar(c):
    print(i)
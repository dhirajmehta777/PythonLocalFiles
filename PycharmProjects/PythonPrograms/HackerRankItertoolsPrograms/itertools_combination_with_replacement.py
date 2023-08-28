from itertools import combinations_with_replacement
s=input().split()
string=sorted(s[0])
num=int(s[1])
print(*list(map(''.join,combinations_with_replacement(string, num))),sep='\n')
s=input('enter string:')
l=s.split()
l1=[]
for word in l:
    l1.append(word[::-1])
res=' '.join(l1)
print(res)
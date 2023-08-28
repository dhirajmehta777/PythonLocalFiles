s=input('enter a string:')
l=s.split()
i=0
l1=[]
for i in range(i,len(l)):
    if i%2==0:
        l1.append(l[i])
    else:
        l1.append(l[i][::-1])
print(' '.join(l1))
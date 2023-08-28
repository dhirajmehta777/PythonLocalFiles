s=input('enter string:')
previous=s[0]
count=1
i=1#we should start from second char
res=''
while i<len(s):
    if s[i]==previous:
        count+=1
    else:
        res=res+str(count)+previous
        previous=s[i]
        count=1
    if i==len(s)-1:
        res = res + str(count) + previous

    i+=1
print(res)


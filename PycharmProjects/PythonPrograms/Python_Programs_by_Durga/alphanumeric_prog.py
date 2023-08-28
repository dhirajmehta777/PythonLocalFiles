s=input('enter string:')
res=''
for ch in s:
    if ch.isalpha():
        x=ch
    else:
        d=int(ch)
        res=res+(x*d)
print(res)
print(''.join(sorted(res)))
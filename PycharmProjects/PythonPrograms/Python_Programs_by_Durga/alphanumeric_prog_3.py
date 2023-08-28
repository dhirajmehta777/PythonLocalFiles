s=input('enter string:')
res=''
for ch in s:
    if ch.isalpha():
        res=res+ch
        x=ch
    else:
        d=int(ch)
        newch=chr(ord(x)+d)
        res=res+newch
print(res)

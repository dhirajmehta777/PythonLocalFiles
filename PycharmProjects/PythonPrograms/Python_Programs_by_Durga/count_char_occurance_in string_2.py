s=input('enter string:')
d={}
res=''
for ch in s:
    d[ch]=d.get(ch,0)+1
for k,v in d.items():
    res=res+str(v)+k
print(res)

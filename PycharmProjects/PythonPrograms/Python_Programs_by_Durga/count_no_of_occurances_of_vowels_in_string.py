s=input('enter string:')
d={}
v={'a','e','i','o','u','A','E','I','O','U'}
for ch in s:
    if ch in v:
        d[ch]=d.get(ch,0)+1
for k,v in sorted(d.items()):
    print('{} occurs {} times'.format(k,v))
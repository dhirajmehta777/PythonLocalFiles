#how to create empty dictiony:
d={}
#how to add key and value pairs in dictionary
d['a']=100
d['b']=200
d['a']=d.get('a')+1#(1+1)
print(d)
#In dictionary duplicate keys are not allowed but values are allowed, if we try to add duplicate key then
#old value will be replaced with new value

#how to fetch values from dict:
print(d.get('a'))#100
print(d.get('z'))#none it wont throw error
#if you dont want none as a output then assign default value to the key
print(d.get('z',0))

#to fetch all the key and value from dictionary:
for k,v in sorted(d.items()):
    print(k,v)

"""
find out occurance of characters in a given string using dictionary concept not using count function
"""
s=input('enter string:')
d1={}
for ch in s:
    d1[ch]=d1.get(ch,0)+1
for k,v in d1.items():
    print('{} occurs {} times'.format(k,v))



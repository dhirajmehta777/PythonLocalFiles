# s=input('enter string:')
# l=[]
# for ch in s:
#     if ch not in l:
#         l.append(ch)
# for ch in sorted(l):#if you want the output in sorted orded then make l to sorted(l)
#     print('{} occurs {} times'.format(ch,s.count(ch)))

#Approach2:
s=input('enter string:')
s1=set(s)
for ch in sorted(s1):#if you want the output in sorted orded then make l to sorted(l)
    print('{} occurs {} times'.format(ch,s.count(ch)))
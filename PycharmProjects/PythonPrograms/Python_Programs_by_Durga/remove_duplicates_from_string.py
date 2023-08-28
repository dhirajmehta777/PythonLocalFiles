# #Approach1:
# s=input('enter string:')
# res=''
# for ch in s:
#     if ch not in res:
#         res=res+ch
# print(res)

# #Approach2:
# s=input('enter string:')
# l=[]
# for ch in s:
#     if ch not in l:
#         l.append(ch)
# print(l)
# print(''.join(l))

#Approach3:
s=input('enter string:')
s1=set(s)
print(''.join(s1))
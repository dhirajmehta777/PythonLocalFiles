# mystr=input("Enter String:")
# dict={}
# for letter in mystr:
#     if letter in dict:
#         dict[letter]+=1
#     else:
#         dict[letter]=1
# print(dict)

from collections import Counter
res=Counter(input('enter string:'))
print(res)
print(dict(res))
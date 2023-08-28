# s=str(input())
# lower= list()
# upper=list()
# even=list()
# odd=list()
# for i in s:
#     if(i.islower()):
#         lower.append(ord(i))
#     elif(i.isupper()):
#         upper.append(ord(i))
#     else:
#         if(int(i)%2==0):
#             even.append(ord(i))
#         else:
#             odd.append(ord(i))
#
# lower.sort()
# upper.sort()
# odd.sort()
# even.sort()
# merge=lower+upper+odd+even
# for i in merge:
#     print(chr(i),end="")

lower=""
upper=""
odd=""
even=""
s=sorted(input())#this will return a list
for i in s:
    if i.islower():
        lower+=i
    elif i.isupper():
        upper+=i
    elif int(i)%2!=0:
        odd+=i
    elif int(i)%2==0:
        even+=i
print(lower+upper+odd+even)

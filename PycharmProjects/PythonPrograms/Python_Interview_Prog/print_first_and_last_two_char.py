# str=input('enter string')
# if len(str)<2:
#     print("Empty String")
# else:
#     s1=str[0:2]
#     s2=str[len(str)-2:len(str)]
#     print(s1+s2)

str=input('enter string')
if len(str)<2:
    print("Empty String")
else:
    print(str[0:2]+str[-2:])

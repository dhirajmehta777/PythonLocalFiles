#Approach1:
# s=input('enter a string:')
# i=0
# # for i in range(i,len(s),2):
# #     print(s[i])
# print('characters present at the even index:')
# while i<len(s):
#     print(s[i])
#     i+=2
# i=1
# print('characters present at the odd index:')
# while i<len(s):
#     print(s[i])
#     i+=2

#Approach2:using slicing
s=input('enter a string:')
print('characters present at the even index:',s[0::2])
print('characters present at the odd index:2',s[1::2])

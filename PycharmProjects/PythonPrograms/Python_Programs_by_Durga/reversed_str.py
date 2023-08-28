#Approach1:using slicing
str=input("enter string:")
reverse_str=str[::-1]
print(reverse_str)

#Approach2:using reversed function
s=input("enter string:")
r=reversed(s)
# for char in r:
#     print(char)
output=''.join(r)
print(output)

#approach3:using while loop
s1=input("enter string:")
o=''
i=len(s1)-1
while i>=0:
    o=o+s1[i]
    i=i-1
print(o)

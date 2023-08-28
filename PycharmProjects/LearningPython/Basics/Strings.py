#String is a collection of character and can be created using single coat or double coat
#Creating Strings:

#Approach1:
s1="ram"
s2='sita'
s3='c'
print(s1,s2,s3)

#Approch2:
n1=str("welcome")
print(n1)

#In python strings are immutable that is once created cannot be modified.
#to know were exacltly the string is stored we have a id() method.
str1="welcome"
str2="welcome"
print(id(str1),id(str2))#139679001458928 139679001458928, these are memory locations of strings
str2=str2+"to python"
print(id(str1),id(str2))#139679001458928 139679001080416 we can see here str2 allocates different location
# hence strins in python are immutable















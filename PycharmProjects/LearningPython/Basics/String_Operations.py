# #+ plus sign is used for concatenation
# #* star is used for repeating the same thing multiple times
# str1="welcome"
# print(str1+" to programming")
# print(str1*3)#printing same string multiple times
#
# #Strinf Slicing:
# #we can take subset of string from original string by using [] operator also known as slicing operator
# #Syntax:s[start:end], this will return part of the string starting from index start to index end-1
# print(str1[1:3])#o/p el
# print(str1[:6])#o/p welcom
# print(str1[4:])#o/p ome
# """
# ord() and chr() functions:
# ord(): function returns the ASCII code of the character.
# chr(): function returns character represented by a ASCII number
# """
# print(ord('A'))#65
# print(chr(65))#A
# """
# len():returns length of the string
# max():returns character having highest ASCII value
# min():returns character having lowest ASCII value
# """
# print(len("hellow"))
# print(max("abc"))
# print(min("abc"))
# """
# in and not-in operator
# we can use in and not in operator to check existence of string in another string
# they are also known as membership operator
# """
# print("come" in str1)#True
# print("come" not  in str1)#False
# print("xyz" in str1)#False
# print("xyz" not in str1)#True
# """
# String Comparision
# we can use(>,<,<=,>=,==,!=) to compare two strings
# Python compare strings lexiographically i.e. using ASCII value of the character
# """
# print("###########################")
# print("tim"=="tie")#F
# print("free" != "freedom")#T
# print("arrow">"aron")#T
# print("right">="left")#T
# print("teeth"<"tee")#F
# print("yellow"<="fellow")#F
# print("abc">"")#T
# """
# Iterating String Using for Loop
# String is a sequence type and also iterable using for loop
# """
s="hello"
for i in s:
    print(s)
print("#####################")
for i in s:
    print(i)
print("#####################")
for i in s:
    print(s,end="\n")#this is default behaviour
print("#####################")
for i in s:
    print(s,end="")#print string without a newline
print("#####################")
for i in s:
    print(s,end="foo")#now print() will print foo after every
"""
Testing Strings 
String class in python has various in build methods which allows to check for different types of strings
"""
import subprocess

print("#################################################################")
x="welcome to pycharm"
print(x.isalnum())#returns True if string is alphanumeric o/p=False
print(x.isalpha())#returns true if string contains only alphabates o/p=False
print("2022".isdigit())#Returns True if string contains only digits o/p=True
print(x.isidentifier())#Returns true if string is valid identifier o/p=False
print(x.islower())#Returns true if string is in lowercase o/p=True
print(x.isupper())#returns true if string is in uppercase o/p=false
print(x.isspace())#returns true if string contains only whitespaces o/p=False
"""
Searching for SubString
"""
print("################################################################################")
print(x.endswith("thon"))#Returns True if strings ends with substring o/p=True
print(x.startswith("good"))#o/p=false
print(x.find("come"))#returns lowest index from where s1 starts in the string, if string not found returns
# -1
print(x.find("become"))#o/p=-1
print(x.rfind("o"))#o/p=15 returns highest index from were s1 starts in the string if string not found returns -1
print(x.count("o"))#returns no of occurence of substring in the string
"""
Converting Strings
"""
s="String in PYTHON"
s1=s.capitalize()#returns a copy of the string with only the first character capitalized
print(s1)
s2=s.title()#this function return string by capitalizing first letter of every word in the string
print(s2)
s3=s.lower()#return string by converting every character into lower case
print(s3)
s4=s.upper()
print(s4)
s5=s.swapcase()#return a string in which lower to upper and upper is converted to lower
print(s5)
s6=s.replace("in","on")
print(s6)








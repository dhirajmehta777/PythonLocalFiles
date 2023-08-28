str1=input("string1:")
str2=input("string2:")
sorted_str1=sorted(str1)
print(sorted_str1)
sorted_str2=sorted(str2)
print(sorted_str2)
if len(str1)==len(str2):
    if sorted_str1 == sorted_str2:
        print("given strings are anagram")
    else:
        print("strings are not anagram")
else:
    print("strings are not anagram")
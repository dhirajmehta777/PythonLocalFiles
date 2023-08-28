#Approach1:this will work only when the length of all the strings are equal
# s1=input("string1:")
# s2=input("string2:")
# s3=input("string3:")
# i=j=k=0
# while i<len(s1) or j<len(s2) or k<len(s3):
#     res=s1[i]+s2[j]+s2[k]
#     print(res)
#     i+=1
#     j+=1
#     k+=1

#Approch2:Modify the code so that it should work if the lengths of all the strings are not same
s1=input("string1:")
s2=input("string2:")
s3=input("string3:")
i=j=k=0
while i<len(s1) or j<len(s2) or k<len(s3):
    res=''
    if i<len(s1):
        res=res+s1[i]
        i+=1
    if j<len(s2):
        res=res+s2[j]
        j+=1
    if k<len(s3):
        res=res+s3[k]
        k+=1
    print(res)
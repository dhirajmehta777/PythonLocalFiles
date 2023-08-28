#Write a function to Reverse string:Input="text1 text2 text3 Output:="text3 text2 text1

str1="text1 text2 text3"
l=str1.split()
l2=l[::-1]
print(' '.join(l2))
UI='$12,000'
u=UI.replace('$','').replace(',','')
print(u)
DB=12000
v=str(DB)
assert v==u
#assert UI==DB
# U=int(UI)
# assert U==DB




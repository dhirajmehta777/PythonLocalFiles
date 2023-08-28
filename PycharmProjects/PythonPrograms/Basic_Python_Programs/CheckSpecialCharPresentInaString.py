import re
str="welcome@@2To%%Python**Programming@!!^%%@$"
str2="welcome to python programming"
regex=re.compile('[@_!#$%^&*()<>?/\|}{~:]')
if(regex.search(str2)==None):
    print("No special character present in a string")
else:
    print("String contains special characters")
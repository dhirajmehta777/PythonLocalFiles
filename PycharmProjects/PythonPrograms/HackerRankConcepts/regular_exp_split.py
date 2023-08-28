import re
s=input("Enter the string")
regex_Pattern=r"[,.]+"
print("\n".join(re.split(regex_Pattern,s)))

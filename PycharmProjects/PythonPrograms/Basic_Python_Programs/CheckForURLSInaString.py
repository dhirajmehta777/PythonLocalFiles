import re
str="Im blogger at http://www.pavantestingtools.com/"
#http://urlregex.com/
url=re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',str)
print(url)
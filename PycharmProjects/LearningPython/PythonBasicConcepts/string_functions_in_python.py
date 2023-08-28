x="     @#$python world python world python world python world     "
print(len(x)) #returns the no of items in an object or if the object is string itwill return
# the length of the string.
y=45846
# print(y.find("84")) #throw error
z=str(y)
print(z)
print(type(z))
print(z.find("84"))#returns the position of sub string
# print(str(y)) #str() converts the specified value into string
# go to google search for python documnetation
# click on documentation
# click on library reference
# Search for str
# click on common string operations
# click on string methods
d=x.upper()
print(d) #converts all the chars into uppercase
"""
count(sub[, start[, end]])
returns a no of times the specified value found in the string
"""
print(x.count("python"))
print(x.count("python", 10,30))

print(d.isupper())#returns true if all the chars are in uppercase
print(d.islower())#returns true if all the chars are in lowercase

"""
split(sep=none, maxsplit=-1)
splits the string at the specified seperator and returns a list
"""
print(x.split()) #here if we dont specify anything it will consider white space as a seperator

"""
there is one more function that is rsplit(), it works same as split but it 
will splits a string into list but starting from right.
"""
#print(x.strip())#strip() retuns trimmed version of string, it will trim whitespaces
#print(x.strip('@,#,$'))
#print(x.lstrip()) remove any leading characters
#print(x.rstrip()) remove any trailing characters
print(x.replace("python", "pycharm"))
print(x.replace("python", "pycharm", 2))
print(x.find("pycharm"))
#print(x.index("pycharm"))
print(x.find("python"))
print(x.index("python"))


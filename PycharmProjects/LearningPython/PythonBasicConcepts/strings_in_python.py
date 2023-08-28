x="welcome 'to' python" #we can use single coat inside the double coat but not double coat
y='welcome "to" pycharm' #we can use double coat inside the single coat but not single coat
z='Hello \'python\' world' #we can use the single coat inside single coat by using escape char i.e \backslash

print(x)
print(y)
print(z)

#Strings are also arrays that is we can get the char by using index
print(y[4])

q="""
this is a 
multiline string
"""
print(q)

e='''
this is also 
multiline string
'''
print(e)
#if i dont assign this string to any variable then it will be treated as comment.

print("is" in q)
print("iss" in q)
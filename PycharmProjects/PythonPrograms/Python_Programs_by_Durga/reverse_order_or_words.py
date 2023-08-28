s=input('enter string:')
l=s.split()#this will split enter string into individual string with , separated list
print(l)#returns list having multiple words with , separated
l1=l[::-1]
print(l1)#here we dont want output in list format we want in string format so,
output=' '.join(l1)
print(output)
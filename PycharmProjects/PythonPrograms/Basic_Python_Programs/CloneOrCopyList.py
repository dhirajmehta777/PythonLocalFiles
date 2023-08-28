#Approach1:Using slicing teschnique
# mylist=[4,5,8,9,6,2]
# mylist_copy=mylist[:]
# print("copy of the list:",mylist_copy)

# #Approach2:using extend() method
# mylist=[4,5,8,9,6,2]
# mylist_copy=[]
# mylist_copy.extend(mylist)
# print("copy of the list:",mylist_copy)

#Approach3:using list() method
# mylist=[4,5,8,9,6,2]
# mylist_copy=list(mylist)#this list method will add the content of the mylist to mylist_copy
# print("copy of the list:",mylist_copy)

#Approach4:using copy() method
# mylist=[4,5,8,9,6,2]
# mylist_copy=mylist.copy()
# print("copy of the list:",mylist_copy)

#Approach5:Using list comprehensions
mylist=[4,5,8,9,6,2]
mylist_copy=[i for i in mylist]
print("copy of the list:",mylist_copy)
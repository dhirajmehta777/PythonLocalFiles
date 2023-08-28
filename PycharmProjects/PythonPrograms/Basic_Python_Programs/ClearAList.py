#Approach1:using clear() meythod
# mylist=[12,33,5,48,50]
# print("my list before clearing",mylist)
# mylist.clear()
# print("my list after clearing",mylist)

#Approach2:initiaizes the list with no value
# mylist=[12,33,5,48,50]
# print("my list before clearing",mylist)
# mylist=[]
# print("my list after clearing",mylist)

#Approach3:using "*=0", this method removes all elements of the list and makes it empty
# mylist=[12,33,5,48,50]
# print("my list before clearing",mylist)
# mylist *=0 #delets all elements from the list
# print("my list after clearing",mylist)

#Approach4:using del keyword
mylist=[12,33,5,48,50]
print("my list before clearing",mylist)
del mylist[:]
print("my list after clearing",mylist)
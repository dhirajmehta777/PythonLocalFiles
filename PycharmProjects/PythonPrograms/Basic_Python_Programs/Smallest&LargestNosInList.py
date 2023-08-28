#Approach1:sort the list in ascending order and print the first and last elements in the list
# mylist=[20,100,20,1,10]
# mylist.sort()
# print(mylist)
# print("smallest element is:",mylist[0])
# print("largest element is:",mylist[-1])

#Approach2:using min() and max() method
mylist=[20,100,20,1,10]
print("smallest element is:",min(mylist))
print("largest element is:",max(mylist))
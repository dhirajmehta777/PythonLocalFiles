#Approach1:sort the list in ascending order and print the first and last elements in the list
# mylist=[20,100,20,1,10]
# mylist.sort()
# print(mylist)
# print("first largest number is:",mylist[-1])
# print("second largest number is:",mylist[-2])

#Approach2:
mylist=[30,100,20,1,10]
new_list=set(mylist)
print(new_list)
new_list.remove((max(new_list)))
print(new_list)
print(max(new_list))
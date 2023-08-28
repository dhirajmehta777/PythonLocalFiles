#Approach1:temporary variable
# mylist=[1,2,3,4]
# size=len(mylist)
# temp=mylist[0]
# mylist[0]=mylist[size-1]
# mylist[size - 1] = temp
# print("list after swapping:",mylist)

#Approach2:
# mylist=[1,2,3,4]
# mylist[0],mylist[-1]=mylist[-1],mylist[0]
# print("list after swapping:",mylist)

#Appraoch3:using tuple
# mylist=[1,2,3,4]
# get=(mylist[-1],mylist[0])
# mylist[0],mylist[-1]=get
# print("list after swapping:",mylist)

#Approach4:using *operand
# mylist=[1,2,3,4]
# start,*middle,end=mylist
# print(start)
# print(*middle)
# print(end)
# mylist=[end,*middle,start]
# print("list after swapping:",mylist)

#Approach5:using pop()

mylist=[1,2,3,4]
first=mylist.pop(0)
last=mylist.pop(-1)
mylist.insert(0,last)
mylist.append(first)
print("list after swapping:",mylist)
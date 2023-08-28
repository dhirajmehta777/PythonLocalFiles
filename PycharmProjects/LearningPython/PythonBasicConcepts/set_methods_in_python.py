set1={"pune", "ranchi", "mumbai", "banglore"}
set2={"pune", "ranchi", "mumbai", "banglore", "chennai"}

print(set1)
set1.add("sydney") #add the item into the set
print(set1)
set1.remove("sydney") #remove the item from the set
print(set1)
set1.discard("pune") #remove the item
print(set1)
set2.pop() # it will remove the item randomly from the set
print(set2)
#set3=set1.union(set2) #union of two sets retuns unique items
#print(set3)

#diff between union and union update
#usually union joins two sets and returns new set
#usually update will update the set1 with set2
set4=set1.update(set2) #in case of update it will not return a new set but it will update the existing set
print(set1)

set5=set1.intersection(set2) #intercestion of two sets retuns duplicate items
print(set5)
set1.intersection_update(set2)
print(set1)

set6=set1.symmetric_difference(set2)#returns excluding duplicates
print(set6)
set1.symmetric_difference_update(set2)
print(set1)

set7=set1.difference(set2)
print(set7)
set8=set2.difference(set1)
print(set8)

set9=set1.issubset(set2)
print(set9)#all the values of set1 is a part of set2 hence it will return true

set10=set1.issuperset(set2) #it will return false bcz set1 is not a super set of set2
print(set10)
set11=set2.issuperset(set1)# it will return true as set2 is a super set of set1
print(set11)


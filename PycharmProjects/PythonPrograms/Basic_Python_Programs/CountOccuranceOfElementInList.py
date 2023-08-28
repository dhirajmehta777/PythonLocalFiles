#Approach1:using loop
# mylist=[15,6,7,10,12,20,10,28,10]
# x=10
# count=0
# for ele in mylist:
#     if ele==x:
#         count=count + 1
# print("{} has occurred {} times".format(x,count))

#Approach2:using count() method
# mylist=[15,6,7,10,12,20,10,28,10]
# x=10
# count=0
# print("{} has occurred {} times".format(x,mylist.count(x)))

#Approach3:using counter()
from collections import Counter
mylist=[15,6,7,10,12,20,10,28,10]
x=10
dic=Counter(mylist)
print("{} has occurred {} times".format(x,dic[x]))
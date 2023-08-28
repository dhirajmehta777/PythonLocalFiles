#list type is another sequence type defined by the list class of python
#list allows you to add, delete or process elements in very simple ways
#list is very similar to arrays that is we can store multiple data of same datatype or different datatype

#Creating Lists
list1=list()#creating an empty list
print(list1)#o/p []

#how we can add values in the list:
list2=list([20,30,50])
print(list2)
list3=list(["tom","jerry","spyke"])
print(list3)
list4=list("python")
print(list4)

#How to access elements from the lists:
#you can use index operator ([]) to access individual elements in the list.list index starts from 0(zero)
l1=[1,2,3,4,5]
print(l1[1])

#list common operations:
l2=[2,5,9,50,100]
print(100 in l2)#o/p=True
print(2 not in l2)#o/p=False
print(len(l2))#o/p=5
print(max(l2))#o/p=100
print(min(l2))#o/p=2
print(sum(l2))#o/p=166

#List Slicing:slice operator ([start:end]) allows to fetch sublist from the list.It works similar to string
print(l2[0:3])#[2,5,9]
print(l2[:4])#if we wont mention any start point it will consider as 0, o/p=[2,5,9,50]
print(l2[0:])#if we wont mention end index it will take till length of the list o/p[2, 5, 9, 50, 100]

#+ and * operators
"""
+--> operator joins two lists
*--> operator replicates the elements in the list
"""
l3=l1+l2
print(l3)
l4=[1,2,3]
print(l4*3)

#Traversing the list using for loop:
#we can use for loop to loop through all the elements of the list.
for i in l2:
    print(i)
   # print(i,end=" ")#if we want to print in the same line

#Commonly used list methods with return type:
l5=[4,2,6,8,9,1]
l5.append(99)#this will additionally append this value at the end of the list
print(l5)#[4, 2, 6, 8, 9, 1, 99]
###########################################################
print(l5.count(4))#1
###########################################################
l6=[85,65,44,77]
l5.extend(l6)
print(l5)#[4, 2, 6, 8, 9, 1, 99, 85, 65, 44, 77] existing as been extended by including l6 items
#############################################################
print(l5.index(8))#3
##########################################################
l5.insert(1,20)
print(l5)#[4, 20, 2, 6, 8, 9, 1, 99, 85, 65, 44, 77]
##############################################################
print(l5.pop(1))#this will return the element to be popped or removed, and removes the element of that index num
print(l5)#if we print the lists that element is removed
##############################################################
l5.remove(99)#remove 99 from the list
print(l5)#[4, 2, 6, 8, 9, 1, 85, 65, 44, 77]
#########################################################
l5.reverse()
print(l5)#[77, 44, 65, 85, 1, 9, 8, 6, 2, 4]
############################################################
l5.sort()#sorted in ascending order
print(l5)#[1, 2, 4, 6, 8, 9, 44, 65, 77, 85]

#list Comprehensions:
for x in range(10):
    print(x)#this will print 0 to 10 but if we want to store those numbers in the
    # list we go for list comprehensions

l8=[x for x in range(10)]#this will create a list containing digits from 0 to 9
print(l8)#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#if we want to store 1 to 10:
l9=[x+1 for x in range(10)]
print(l9)#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#if we want to print even numbers:
l10=[x for x in range(10) if x%2==0]
print(l10)









































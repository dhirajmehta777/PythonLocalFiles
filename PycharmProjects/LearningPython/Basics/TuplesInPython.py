#Tuples are very similar to list but once a tuple is created,
# you cannot add, delete, replace reorder elements
#Tuples are immutable
t1=()#empty tuple with no elements
t2=(2,3,4,5,6)
t3=([4,5,6,8,9,7])#tuple containing list of elements
t4=tuple("abc")#this will convert string into multiple characters
print(t1)#()
print(t2)#(2, 3, 4, 5, 6)
print(t3)#[4, 5, 6, 8, 9, 7]
print(t4)#('a', 'b', 'c')

"""
Tuple Functions:
Functions like max, min, len, sum can also be used with tuples
"""
print(min(t2))
print(max(t3))
print(sum(t3))
print(len(t4))

"""
Iterating through tuples:
tuples are iterable using for loop
"""
print("####################################")
for i in t2:
    print(i)
   # print(i,end=" ")prints in the same line
"""
Slicing tuples
Slicing operators works same in tuples as in list and string
"""
print(t2[0:2])
print(t2[2:4])
print(t2[0:])
print(t2[:4])
print(t2[:])
"""
in and not in operator:
we can use in and not in operators to check existence of item in tuples
"""
print(2 in t2)#True
print(7 not in t2)#True



































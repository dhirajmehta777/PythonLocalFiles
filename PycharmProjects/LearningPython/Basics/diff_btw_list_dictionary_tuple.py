"""
Lists:
list=[0,1,2,3]
print([0])
Allows duplicates
list[0]=100, lists can be modified i.e, we can add element at specific index
lists are mutable
lists can be created using [] bracket
slicing can be done, list=[20,30,50],print(list[1:2])#30
Usage:use list if you have a collection of data that doesnt need random access.
use list when you need a simple, iterable collection that is modified frequently
"""

"""
Dictionaries:
Dict={"john":"25","marry":60}
print(dict["Marry"])
Duplicate keys are not allowed but duplicate values are allowed.
dict["john"]=55
Dictionaries are mutable.
Dictionary is created use {} curly braces
Slicing cant be done
Usage:When you need a logical association between key:value pair.
when you need fast lookup for your data based on a custom key.
"""

"""
Tuples:
tup1=("10,20,30") or tup1=10,20,30
tup3=("john","scott") or tup4="john","scott"
print(tup1[0])
Allows duplicates faster then lists
tup1[0]=100#type error since tuples are immutable
Immutable:values can't changed once assigned
tuples can be created using ()
slicing can be done, tup=(10,20,3,4,5,6,7), print(tup[2:4]) #(3,4)
Usage:use tuples when your data cannot change.
A tuple is used in combination with dictionary, for example 
a tuple might represent a key, because its immutable
"""
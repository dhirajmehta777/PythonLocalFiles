#Dictionary is a python data type that is used to store key value pairs
#ie enables you to quickly retrieve, add, modify values using key.
#Dictionary is very similar to HashMap in java.
#Dictionaries are mutable

"""
Dictionaries can be created using pair of curly braces({}).
Each item in the dictionary consists of key followed by a colon, which is followed by a value.
And each item is seperated using commas (,).
key must be hashable type, but value can be of any type, each key in the dictionary must be unique.
"""
d1={'tom':'11-222-999','jerry':'222-888-55'}
print(d1)

#Retrieving, modifying and adding elements in the dictionary:
#Retrieving elements from the dictionary
print(d1['tom'])#o/p 11-222-999

#Adding elements into the dictionary:
d1['bob']='555-444-777'
print(d1)#{'tom': '11-222-999', 'jerry': '222-888-55', 'bob': '555-444-777'}

#Modify elements into the dictionary:
d1['bob']='888-777-666'
print(d1)#{'tom': '11-222-999', 'jerry': '222-888-55', 'bob': '888-777-666'}

#Delete element from the dictionary:
del d1['bob']
print(d1)#{'tom': '11-222-999', 'jerry': '222-888-55'}

#Looping items in the dictionary:
values={'a':'100',
        'b':'200',
        'c':'300',
        'd':'400'}
for k in values:
    print(k, ":", values[k])

#find the length of the dictionary:
print(len(values))

"""
Equality Tests in dictionary
== and != operators tells weather dictionary contains same items or not
Note:you cant use other relational operators like <,>,>=,<= to compare dictionaries
"""
d2={"mike":41, "bob":3}
d3={"bob":3, "mike":41}
print(d2==d3)#True
print(d2!=d3)#False

#Dictionary Methods:

#popitem() returns randomly select item from dictionary and also remove
print(d1.popitem())
print(d1)

#clear() deletes every thing from the dictionary:
d1.clear()
print(d1)

#keys() return keys in the dictionary as tuple:
print(d2.keys())#dict_keys(['mike', 'bob'])

#values() return values in dictionary as tuple:
print(d2.values())#dict_values([41, 3])

#get(key) return value of key, if key is not found it returns none, instead on throwing keyerror exception
print(d2.get('mike'))

#pop(key) remove the item from the dictionary, if key is not found keyerror will be thrown
d2.pop('mike')
print(d2)


































































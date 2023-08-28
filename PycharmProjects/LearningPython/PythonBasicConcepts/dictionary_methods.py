dict1={'name1':'ram', 'job':'qa', 'city':'pune', 4:'uat'}
print(dict1.get("job")) #returns the value for the key specified
print(dict1.keys())#returns all the keys available in the dictionary
print(dict1.items())#returns list and list contains tuples within the dictionary
print(dict1.values())#returns all the values available in the dictionary
print(dict1.pop(4))#removes value for the specified key from the dictionary

#from python 3.7 the dictionaries are ordered and before 3.7 its unordered hence
#if we use popitems function it will remove last item only
print(dict1.popitem())
dict1.update({"lang":"python"})#add key value pair to the dictionary
print(dict1)

dict1_copy=dict1.copy()
print(dict1_copy)#creates copy of exixting dictionary
dict1_copy.clear()
print(dict1_copy)#prints empty dictionary
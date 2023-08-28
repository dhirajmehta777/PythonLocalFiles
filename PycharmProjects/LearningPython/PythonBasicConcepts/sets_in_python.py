#sets are unordered and will not accept duplicates.
#the main usage of set is membership testing and eliminating the duplicates.
#sets are defined using curly braces{}
#set doesn't holds any specific ordered

set1={10,20,20,30,40}
set2={10,10.5,"ram","s"}
set3={"python", "java", "10", "30"}
set4=set(("45","50","60","25.3"))

print(set3)
print(set1) #eliminated 20 since its a duplicate and printed only one value
#if you want to create empty set we need to use set() function not the curly braces
#if you use it then it will create dictionary.
print(set4)
print(len(set4)) #it will not count duplicate values only counts unique values
print(20 in set1)


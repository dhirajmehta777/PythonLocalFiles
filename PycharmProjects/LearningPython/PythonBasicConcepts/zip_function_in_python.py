#go to official python documentation page
#click on reference library
#go to the build in functions
#in build in function you will be seeing zip() function click on it
#zip function will take the iterable basically iterables are lists, touple etc
#suppose if you pass on two lists with a zip function, it will map the values from list1 and list2
#and it will give output that is it will return a iterator
#it will take arrguments in the form of tuples lists etc.


list1=["India", "Australia", "USA", "UK"]
list2=["pune", "melbourne", "newyork", "london", "sydney"]
s=zip(list1,list2)
print(s) #returns an zip object
print(list(s))#if we want to see the mapped values then we can store these into the list
#after mapping it will return tuple
# if list2 has additional item compare to list1 then zip function will ignore that item
#prints only those items which are mapped

# for x,y in zip(list1,list2):
#     print(x,y)
#
# total_cost=[45,55,66,77]
# sales_price=[77,88,99,85]
#
# for a,b in zip(total_cost,sales_price):
#     print(b-a)

t1={11,22,33,44}
s1={44,55,66,77}
print(t1)
print(s1)
for e,f in zip(t1,s1):
    print(f-e)#here in sets it will substract randomly not in order bcz sets are unordered

list3={"India", "Australia", "USA", "UK"}
list4={"pune", "melbourne", "newyork", "london", "sydney"}
for h,g in zip(list3,list4):#here its a set so it will map the values randomly
    print(h,g)
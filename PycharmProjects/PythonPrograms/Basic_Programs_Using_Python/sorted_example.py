list1=[7,5,4,8,2,1,6]
tuple1=((3,8),(2,9),(1,10),(4,7))
d1={3:"e",2:"a",1:"c",7:"b",5:"d"}
print(sorted(list1))#sort the list in ascending order
print(sorted(list1,reverse=True))#sort the list in descending order
print(sorted(tuple1))
print(sorted(tuple1,reverse=True))
print(sorted(d1))
print(sorted(d1.values()))
print(sorted(d1.items()))#this will sort the dictr w.r.t key
print(sorted(d1.items(),key=lambda x: x[1]))#this will sort the dictr w.r.tvalue

tuple2=((1,'a'),(4,'s'),(3,'z'),(2,'r'))
print(sorted(tuple2))
def secondvalue(element):
     return element[1]

print(sorted(tuple2,key=secondvalue))

#tuples are indexed, allow duplicate values and cannot be modified(immutable)
tuple1=(2,3,4,5,6)
tuple2=("python", "python", "c++", "java", "selenium")
tuple3=(True, False, False, True)
tuple4=(True, 1, "delhi", 10.5)

print(tuple4[0])
print(tuple2[1]) #allows duplicate

# print(tuple4.append("pune")) #tuples are immutable they cannot be modified,
#once tuple object is created cannot be modified

# print(tuple4.pop()) #we cannot pop the tuble since its immutable

print(len(tuple4)) #prints length of the tuple
print(type(tuple3))
print(tuple2.count("python"))
print(tuple2.index("c++"))

for x in tuple4:
    print(x)

joined_tuple=tuple1+tuple2+tuple4 #joins multiple tuples.
print(joined_tuple)
print(type(joined_tuple))
print(tuple2[0:3])

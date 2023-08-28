tuple1=(10,20,30,40,5)
x=max(tuple1)
y=min(tuple1)
print(x)
print(y)

tuple2=(1,2,3,4,5,6)
i=iter(tuple2)
print(next(i))
print(next(i))
print(next(i))
print("#################################")
j=reversed(tuple2)
print(next(j))
print(next(j))
print(next(j))

#######################################
#slice funcion
d=slice(1,3,1)
print(tuple2[d])

############################################
#sorted
c=sorted(tuple1)
print(c)

##########################################
#sum()
#f=sum(tuple2)
f=sum(tuple2,1)#it will add 1 to the total sum of the iterator
print(f)

############################################
#input()
l=input("enter the name: \n")
print("welcome "+l)
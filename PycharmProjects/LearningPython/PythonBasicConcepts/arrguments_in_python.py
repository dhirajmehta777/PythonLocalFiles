"""
positional argument:this arrgument depend on the position that they occur on function thats been called
keyword arrgument:50,30
required arrgument:x,y
optional arrgument:how to make it optional arrgument by assigning values to the parameters while defining
the function
"""
# def substract(x,y):
#     return x-y
# substract(50,30)
#here x,y are parameters and 50,30 are called arrguments

def substract(x=50,y=30):
    return x-y
# z=substract()#here arrguments are optional as its defined while creating the function.
#here it will take default value i.e 50 and 30
# print(z)

z=substract(100)#here you can provide single arrgument also as its optional,
# this single value will assign to x
print(z)
print(substract())#optional takes default values i.e. 30,50
print(substract(100))#optional
print(substract(100,50))#optional, here it will not take default values i.e50,30
print(substract(y=100))#keyword arrgument bcz it will assign to y only


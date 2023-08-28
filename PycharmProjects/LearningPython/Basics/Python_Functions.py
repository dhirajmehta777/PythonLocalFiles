
"""
Functions in Python:
"""
"""
Functions are the reusable pieces of code which help us to organize structure of the code.
We create functions so that we can run a set of statements multiple times during in the program
without repeating oueselves 
"""
"""
Creating Functions.
Functions with return value
Syntax:
def Myfun():
    #statements
"""
def myfun():
    pass#if you dont want to mention any statements then you can only use pass keyword which will
    # ommit body of the function
myfun()#we can call the function in this manner

"""
Ex:2
"""
# def sum(start, end):
#     result=0
#     for i in range(start, end+1):
#         result=result+i
#     print(result)
# sum(0,3)

"""
Ex3:same above example we can do it by using return keyword
"""
# def sum(start, end):
#     result=0
#     for i in range(start, end+1):
#         result=result+i
#     return result
# S=sum(0,3)
# print(S)
"""
Ex4:
"""
def sum(start, end):
    if(start>end):
        print("start should be less then end")
        return
    result=0
    for i in range(start, end+1):
        result=result+i
    return result
S=sum(6,3)
print(S)

"""
Ex5:Without providing return keyword it will still provide the none output
"""
def show():
    i=100
print(show())

"""
Global Variables V/S Local Variables
Global Variables:Variables that are not bound to any function, but can be accessed inside as well as 
outside the function are called global variables.
Local Variables:Variables which are declared inside a function are called local variables
"""
"""
Ex1:
"""
global_var=12
def funct():
    local_var=100
    print(global_var)
funct()
"""
Ex2:
"""
xy=100
def cool():
    xy=10
    print(xy)#10
cool()
print(xy)#100 bcz this print statement is outside the def function
"""
Ex3:
"""
t=1
def increment():
    global t
    t=100
    print(t)
increment()
print(t)
"""
Ex:Pasing argumnets with default values(positional)
"""
def func(i,j=100):
    print(i,j)
#func(50)#50 100
func(50,250)#here j changed from 100 to 250

"""
Ex:passing keyword argument
"""
def named_args(name,greetings):
    print(greetings+" "+name)
named_args("pavan","Hi")#these are positional arguments o/p Hi pavan
named_args(name='pavan',greetings='Hi')#keyword arguments
named_args(greetings='Hi', name='pavan')#keyword arguments

"""
Ex:by combining positional and keyword arrgument
"""
def my_func3(a,b,c):
    print(a,b,c)
my_func3(10,20,30)
my_func3(10,b=20,c=30)
my_func3(10,c=30,b=20)
#my_func3(10,b=20,30)#here this cant be allowed bcz keyword arrguments should be specified at last not in between the positional arrgument
#positional arrgumnet must appear before keyword arrgument, hence this statement is incorrect
"""
Returning multiple values from a function:
We can return multiple values from function using the return statement by separating them with comma(,).
Multple values are returned as tuples
"""
def bigger(a,b):
    if a>b:
        return a, b
    else:
        return b,a
s=bigger(30,10)
print(s)
print(type(s))
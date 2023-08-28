"""
What is *args?
* representing the multiple values and args is a variable name
*args allows us to pass variable number of arguments to the function.
def sum(a,b):"
    print("sum is:"+a+b)
these program only accepts two numbers what if you want to pass more then two numbers,
these is were *args comes into play
Note:name of *args is just a cpnvention  you can use anything that is a valid identifier  for ex:*myargs
"""
def sum(*args):
    s=0
    for i in args:
        s+=i
    print("Sum is : ",s)
sum(1,2,3,4,5)#so this args function will accept any number of values or arguments

"""
Ex2:using list
"""
def my_three(a,b,c):
    print(a,b,c)
args = [1,2,3]
my_three(*args)

"""
What is **kwargs?
this will allows us to pass variable numberof keyword argument:
ex:func_name(name='tim',team='school')
Ex1:
"""
def my_three1(a,b,c):
    print(a,b,c)

a={'a':"one",'b':"two",'c':"three"}
my_three1(**a)
"""
Ex2:
"""
def my_func(**kwargs):
    for i,j in kwargs.items():
        print(i,j)
my_func(name='tom',sport='football',roll=10)#here we can pass multiple key and value pairs as ** represents multiple key vslue pairs

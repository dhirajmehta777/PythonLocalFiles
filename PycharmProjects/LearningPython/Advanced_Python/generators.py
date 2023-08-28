"""
Generators:
"""
"""
Decorator is a function responsible for to enhance the existing functionality by producing a new method with the
help of existing method.
Decorator is always going to take some input function and it will provide some output function.
The output function is more powerfull then input function
the output function is having more enhanced functionality then input function such type of thing is nothing but
decorator functions.

In the same way generator function will not take any input function just it is responsible to generate a sequence 
of values.
How the generators will generate a sequence of values internally by the help Yeild keyword

"""
"""
Example:01
"""
# def mygen():
#     yield 'A'
#     yield 'B'
#     yield 'C'
#
# g=mygen()
# print(type(g))
# print(next(g))
# print(next(g))
# print(next(g))
#print(next(g)) here we are going to get stop iteration error

"""
The biggest advantage of generators is performance will be improved and memory utilization will be improved.
If user dont want to store the huge amount of values whenever its needed it has to generate those values
so here the generator concept comes into picture.
"""

"""
Example1:
"""
# import time
# def countdown(num):
#     print('Count down starting....')
#     while num>0:
#         yield num
#         num=num-1
# values=countdown(10)
# for x in values:
#     print(x)
#     time.sleep(2)

"""
Example2:
"""
# l=(x*x for x in range(1000000000000000000000000000000000000000000000000000))
# print(l) #this will through memory insufficient error.
# l=(x*x for x in range(1000000000000000000000000000000000000000000000000000))
# while True:
#     print(next(l))
#here the values are not stored into the memory instead it will generate the values when needed this will improve memory utilization.
#here yield keyword is internally taken care by the tuple comprehenssions

"""
Example3:To generate first n numbers
"""
# def firstn(num):
#     n=1
#     while n<=num:
#         yield n
#         n=n+1
# for x in firstn(10):
#     print(x)
"""
Where ever you want a sequence of values better to go for generators rather then going for lists
"""
"""
Example:To generate fibonacci numbers:
"""
def fib():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b
for n in fib():
    if n>100:
        break
    print(n)
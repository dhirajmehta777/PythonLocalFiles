import Operations
#here by imorting this file here in main python file we can access the methods which are present in
#that operations python file.
Operations.add(20,20)
Operations.multiply(20,10)

#Approach2:
from Operations import add, multiply
add(20,30)
multiply(30,10)

#Approach3:
from Operations import *
add(10,20)
multiply(10,20)

#################################################

"""
Ex2:Approach 1
"""
import Animal
import Bird

Animal.fly()
Animal.color()
Bird.fly()
Bird.color()

"""
Ex:2 Approach2
"""
# from Animal import *
# from Bird import *
#
# fly()#here which ever function imported last, the methods belonging to that file will execute first,
#o/p Bird can fly, to solve this conflict we can do in this way

from Animal import *
fly()
color()
from  Bird import *
fly()
color()

"""
Ex3:Approach1, containing class and methods
"""
import a
import b

obj1=a.Animal1()
obj1.display()

obj2=b.Bird1()
obj2.display()

"""
Ex3:Approach2, containing class and methods
"""
from a import Animal1
from b import Bird1

obj3=Animal1()
obj3.display()

obj4=Bird1()
obj4.display()

"""
Ex4:containing multiple classes and multiple methods
"""
import m

print(dir(m))#this will return how many classes are there inside m module or python file
#here by using this command we can see how many classes are created inside the module but we cant see
# how many methods are created inside the module.

#if we run the same command by modifying module m i.e placing methods outside of the class and removing
# created class and then these methods are now converted to functions and these functions are counted
# by dir() command



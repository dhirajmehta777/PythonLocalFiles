class MyClass:
    def m1(self):
        print("good morning")
    def __init__(self):#this will initialize automatically once we create an object
        print("this is a constructor")
obj=MyClass()
obj.m1()

"""
Ex2:Converting local variables into class variables
"""
# class MyClass1():
#     def values(self,val1,val2):#here val1 and val2 are local variables and can be accessed within
#         # that method and can't be accessed into another method for that we need to convert the
#         # local variables into class variables.
#         print(val1)
#         print(val2)
#
#     def add(self):
#         print(val1+val2)#here we cannot use local variable in another method so first we need to convert
#         # local to class variable then only we can use those local variables in this method
# obj2=MyClass1()
# obj2.values(10,20)
# obj2.add()# print(val1+val2)#here we cannot use local variable in another method so first we need to convert
# #NameError: name 'val1' is not defined, error will be thrown, if we try to use local variables
# # inside another method

"""
Ex3:
"""
# class MyClass1():
#     def values(self,val1,val2):
#         print(val1)
#         print(val2)
#         self.val1=val1#converted local to class variable and now we can use these variables in another method
#         self.val2 = val2#Converted local to class variable
#
#     def add(self):
#         print(self.val1+self.val2)
# obj2=MyClass1()
# obj2.values(10,20)
# obj2.add()

"""
Ex4:Instead of def values method we can make this as a constructor, so that we no need to call 
this separatly bcz as we create an object it get executed.
"""
class MyClass1():
    def __init__(self,val1,val2):
        print(val1)
        print(val2)
        self.val1=val1#converted local to class variable and now we can use these variables in another method
        self.val2 = val2#Converted local to class variable

    def add(self):
        print(self.val1+self.val2)
obj2=MyClass1(10,20)
#obj2.values(10,20) no need to call this seperately as its a constructor which gets automatically
# gets executed as we create an object, that is constructor will automatically invoke at the time
# of object creation
obj2.add()

"""
Ex5:how to call current class method in another method
"""
class MyCls:
    def m3(self):
        print("this is m1 method")
        self.m4(100)

    def m4(self,a):
        print("this is m2 method",a)

obj3=MyCls()
obj3.m3()

"""
Ex6:Constructor with local variable arguments
"""
# class Mycls1:
#     def __init__(self,name):
#         print(name)
# obj4=Mycls1("pavan")
"""
Ex7:constructor with local and class variable
"""
class Mycls1:
    name="kumar"
    def __init__(self,name):
        print(name)
        print(self.name)
obj4=Mycls1("pavan")

"""
Ex8:Constructorwith multiple arguments
"""
# class Emp:
#     def __init__(self,eid,ename,esal):
#         self.eid = eid
#         self.ename = ename
#         self.esal = esal
#     def display(self):
#         print("Empid:{} Empname:{} Empsal:{} ".format(self.eid,self.ename,self.esal))
#         print("Empid:%d Empname:%s Empsal:%g"%(self.eid,self.ename,self.esal))
# e1=Emp(101,'smith',100000)
# e1.display()

"""
Ex:9 __str__ is a method which will automatically invoke while printing the reference variable
"""
# class MyCls2:
#     pass
# c=MyCls2()#Here c is the reference variable
# print(c)#this will return the memory location of this particular object but who is rturning internally this is done internally by __str__ method

class MyCls2:
    def __str__(self):#and one more thing this __str__ will return only string bcz if we return 10 it will throw error
        # return 10 this will throw error as __str__ method was only returning string value
        return  "welcome"
c=MyCls2()
print(c)#Now this time it will print welcome as it has overriden the internal str method which was previosly printing the memory location of object

"""
Example for __str__ method
"""
class Emp:
    def __init__(self,eid,ename,esal):
        self.eid = eid
        self.ename = ename
        self.esal = esal
    def __str__(self):
        return ("Empid:{} Empname:{} Empsal:{} ".format(self.eid,self.ename,self.esal)) #in this example istead of printing we need to return this values

e1=Emp(101,'smith',100000)
print(e1)

"""
__str__, its a method which will be invoked when ever you print the refernce variable
__init__, its a constructor will be invoked automatically at the time of object creation.
__del__, dell will be automatically invoke when ever you destroy the object
"""

"""
Ex for __del__:
"""
class Del:
    def __del__(self):
        print("Destroyed")
s1=Del()
s2=Del()

del s1#when ever we are destryoing the object del function automatically executes

"""
What is Encapsulation?
In an object oriented python program, you can restrict access to methods and variables.
This can prevent the data from being modified by accident and is known as encapsulation
Encapsulation can be achieved by using private variables and methods
Here in python we can declare the variables and methods as private by specifying __(two underscores) in front
of the variables and methods
"""
"""
Scope of private variables and methods:
public methods:Accessible from anywere
private methods:Accessible only in there own class, starts with two underscores
public variables:Accessible from anywere
private variables:Accessible only in there own class or by a method if defined, starts with __
"""
"""
Ex1:Private Variables can be access only within the method 
"""
class MyClass:
    __a=10#this variable only can be accessed within the class or within the method of that specific class
    def disp(self):
        print(self.__a)
obj1=MyClass()
obj1.disp()

#if we try to access outside of the class it will through an error
#print(MyClass.disp())#the private variable we cannot access outside of the class

"""
Ex2:Private methods only can be accessed only with in the method
"""
class MyClass1:
    def __disp1(self):
        print("this is display1 method")

    def disp2(self):
        print("this is display2 method")
        self.__disp1()#we have to call above private method within this method as we cannot call private method outside of the class

obj2=MyClass1()
obj2.disp2()#we can call only non private methods outside of the class but wer as private methods can't be accessed outside of the class

"""
Ex3:we can access private variables outside of the class indirectly by using some methods
"""
class MyClass2:
    __empid=101
    def getempid(self, eid):
        self.__empid=eid

    def displayempid(self):#this method has been created to access the private variable outside of the class
        print(self.__empid)

obj3=MyClass2()
obj3.getempid(105)#if we call this method we need to pass a parameter and the new value is assigned to empid
obj3.displayempid()#in this way we can idirectly access the private variable by defining additional method




"""
What is Polymorphism?
Sometimes object comes in many types or forms.
if we have a button, there are many different draw outputs(round button, check button, square button, button
with image) but they do share the same logic:onclick().
we access them using the same method. this idea is called polymorphism.
Polymorphism in python can be achieved by using overloading and overriding methods.
"""
"""
Method Overriding:
Override means two methods having same name but doing different tasks.
It means that one of the methods overrides the other.
If there is any method in the superclass and  a method with a same name in a subclasss,
then by executing the method, the method of the corresponding class will be executed
"""

"""
Ex1:Overriding a Variable
"""
class Parent:
    name="scott"
class Child(Parent):
    name="David"
obj=Child()
print(obj.name)#Since variable name is same, hence the child class variable overrides the parent cls variable

"""
Ex2:Overriding a Methods
"""
class Bank:
    def rateofinterest(self):
        return 0
class ICICI(Bank):
    def rateofinterest(self):
        return  10.5
obj1=ICICI()
print(obj1.rateofinterest())#in this we have overrided the method hence it will call latest method of child

"""
Ex3:Method Overloading:
In python you can define a method in such a way that there are multiple ways to call it.
Given a single method or function, we can specify the number of parameters our self
"""
class Human:
    def sayHello(self, name=None):
        if name is not None:
            print("Hello "+name)
        else:
            print("Hello")
o1=Human()
#o1.sayHello("Pavan")  #Hello pavan, since we have passed a parameter so the name will not be None
o1.sayHello()#Hello, bcz we did not pass any parameter hence the will be none so else part will execute
#By this way the same method will behave in two different ways

"""
Ex4:Method Overloading
"""
class Bird:
    def fly(self, name=None):
        if name=="Parrot":
            print("Can Fly")
        if name=="penguine":
            print("Cannot Fly")
        if name==None:
            print("No input")
o2=Bird()
#o2.fly()#No input
o2.fly("Parrot")#Can Fly
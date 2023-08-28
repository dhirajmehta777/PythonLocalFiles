"""
Abstract classes are the classes that contain one or more abstract methods.
An abstract method is a method that is declared, but contains no implementation.
Abstract classes cannot be intantiated and require subclasses to provide implementations for the abstract methods
Subclasses of an abstract class in python are not required to implement abstract methods of parent class
"""
#ABC is a pre defined Abstract class
from abc import ABC, abstractmethod
"""
Ex1:Abstract Class
"""
class A(ABC):
    @abstractmethod
    def display(self):#since its abstract method we haven't implemented any body within this method
        None
        #if we want to implement this abstract method then we need to create one more class

class B(A):
    def display(self):#Abstract methods implementation has been done in this class and then it has been accessed by creating
        # object of this class
        print("this is display method")

obj=B()
obj.display()
#When we need to go for this concept when you know the requiremnents and dont know the design part

"""
Ex2:Abstract Class
"""
class Animal:
    @abstractmethod
    def eat(self):
        pass

class Tiger(Animal):
    def eat(self):
        print("Eats veggies")

class Cow(Animal):
    def eat(self):
        print("Eats Burger")

#here we cannot instantiate Animal class as its an abstract class, so for that we have instantiated tiger and cow class to access the implemented method of abstract class
t=Tiger()
t.eat()
c=Cow()
c.eat()
#here we can implement abstract method in multiple classes also

"""
Ex3:Abstract Class
"""
class X(ABC):
    @abstractmethod
    def m1(self):
        pass
    @abstractmethod
    def m2(self):
        pass

class Y(X):
    def m1(self):
        print("this is m1")
#here if we implement only one method from absttract class then at that time we cannot create object of
# this subclass, so its cumpulsory to implement all the abstract methods of abstract class into the
# subclass then only we can able to create an object of subclass and also we can able to accesss and
# call those methods as well
# y=Y()
# y.m1()#TypeError: Can't instantiate abstract class Y with abstract methods m2
class Z(Y):
    def m2(self):
        print("this is m2")
z=Z()
z.m1()
z.m2()

"""
Ex:4 How to create constructor in abstract class and how we can access it
"""
class Cal(ABC):
    def __init__(self, value):#constructor
        self.value=value#here we have converted local variable to class variable

    @abstractmethod
    def add(self):
         pass
    @abstractmethod
    def sub(self):
         pass

class C(Cal):
    def add(self):
        print(self.value+100)

    def sub(self):
        print(self.value - 10)
c=C(100)
c.add()
c.sub()





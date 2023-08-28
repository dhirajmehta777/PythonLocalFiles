"""
Class is a logical entity which contains logic.
Class contains variables and methods.
Logic should be included within a meyhod.
A class is a blueprint of an object.
class will not occupy any space or memory

An object is a physical entity which is created for a class.
we can create any number of objects for a class
object will occupy memory

class is a collection of variables and methods in order to access them we have to create an object.
"""
"""
Ex1:Creating basic class and object which include methods.
"""
#How to declare a class, class ClassName
class MyClass:#this is the basic class along with two methods
    def myfunc(self):#here self is basically a keyword which says like this function is belongs to this particular class
        pass#if you dont want to write any body inside method then you can write pass keyword which will ommit the body of the method

    def display(self, name):#this method takes a parameter
        print("Name is:",name)

mc=MyClass()#object of the class has been created, here mc is reference variable and myclass() is an exact object this will create a memory location that memory locationwill be identified or reffering by the reference variable
mc.myfunc()
mc.display('scott')

"""
Here we have created a class called MyClass which contains two methods one is myfunc and display.
after creation of class, if we want to use this class we must create an object, through objects only 
we can call these two methods.
Every method or function in a class by default will take one keyword called as "self", 
here self represting these methods are belongs to this particular class.
"""
"""
Diff between function and method in python
technically both are same but therotically they differ.
without class if we define a piece of code thats called as a function,
if we define a piece of code inside any class then we call that as a method.
but in python we can create both ways i.e, if create a function within class that is a method 
and if create a function outside a class that is called as a pure function
"""

"""
Ex2:Instance Method and Static Method
"""
class MyClass2:
    def m1(self):
        print("Instance Method")#when we create a method within a class by default that is a instance method.
        #if we want to call this instance method, we can call through an object.

    @staticmethod
    def m2():#by default static method doesn't take any parameter, even self keyword also
        print("Static Method")#static methods can be directly called by using class name we no need to create an object of the class
        #in python we dont have static variable but in java we have static varieables
mcobj = MyClass2()
mcobj.m1()#instance Method
MyClass2.m2()#if staticmethod takes self keyword as a parameter then it will throw an error, MyClass2.m2()#if staticmethod takes self keyword as a parameter then it will throw an error, so we need to remove that default self keyword from the paranthesis of def function m2
"""
instance method requires self keyword wereas static method doesn't require self keyword
to access the instance method we need to create an object but were as static method can be called directly by using classname.methodname, it doesn't require creation of an object
in case of static method if we use self keyword, that will be treated as an argument, so while calling we need to pass some parameter.
but if we use the self keyword in instance method it is not treated as argument, there it will tell us that this particular method belongs to this particular class,
hence in static self is not required 
def me(self)
MyClass2.m2(10) while calling static method if we are using self keyword in function then while calling 
we must provide some parameter say 10 or 20 anything to execute the function properly otherwise it will 
throw an error instead dont use the keyword self then we no need to pass a parameter while calling the function
"""

"""
Ex3:Static method with parameter
"""
class MyClass3:
    def m1(self):
        print("Instance Method")

    @staticmethod
    def m2(self):
        print("Static Method")
mcobj1 = MyClass3()
mcobj1.m1()#instance Method
MyClass3.m2(10)

"""
Ex4:Declaring Variables inside the class
"""
class MyClass5:
    a,b=100,200   #class variables can be accessed by using self keyword directly we can't access

    def add(self):
        print(self.a+self.b)

    def mul(self):
        print(self.a*self.b)

obj=MyClass5()
obj.add()
obj.mul()

"""
Ex5:Local Variables, Class Variables & Global Variables
"""
#Local Variables:Variables declared within the method. and accessed only within this method
#Class Variable:Variables declared within the class. can be accessed only by using self keyword
#Global Variables:Variables declared outside the class.

i,j=15,25  #Global Variables
class MyClass6:
    s,t=10,20 #class variables
    def add(self, x, y): # x,y are local variables
        print(x+y)#here we accessing directly local variables not required any self keyword
        print(self.s+self.t)#here we are accessing class variables by using self keyword
        print(i+j)#here we are accessing directly global variables
obj2=MyClass6()
obj2.add(100,200)

"""
Ex6:Local Variables, Class Variables & Global Variables with same variable name.
"""
u,v=15,25  #Global Variables
class MyClass7:
    u,v=10,20 #class variables
    def add(self, u, v): # x,y are local variables
        print(u+v)#here we accessing directly local variables not required any self keyword
        print(self.u+self.v)#here we are accessing class variables by using self keyword
        print(globals()['u']+globals()['v'])#here we are accessing directly global variables,
        # since we have same name variable name for local and global to differentiate
        # we have used globals() function keyword to avoid conflict

obj3=MyClass7()
obj3.add(100,200)

"""
Ex7:Creating multiple objects for one class
"""
class MyClass8:
    def disp(self):
        print("GM")

o1 = MyClass8()
o1.disp()
o2 = MyClass8()
o2.disp()
#Here created multiple objects and these objects will be occupying different memory locations
#Every objects are independent and we can easily find the memory locations of these objects by using ID function

"""
Ex8:Named Object and Nameless object
"""
class MyClass9:
    def disp1(self):
        print("GM")

o3 = MyClass9()#Named Object
o3.disp1()
MyClass9().disp1()#Nameless Object

"""
Ex9:How to check memory locations of an objects
"""
class MyClass10:
    def m5(self):
        pass

c1=MyClass10()
c2=MyClass10()
c3=c1

print(id(c1))
print(id(c2))
print(id(c3))

"""
140048633398320
140048633398368
140048633398320
here c1 and c3 will be pointing to the same location
"""
#to check c1, c2 and c3 are same
print(c1 is c2)#this will return False
print(c1 is c3)#True

print(c1 is not c2)#True
print(c1 is not c3)#False
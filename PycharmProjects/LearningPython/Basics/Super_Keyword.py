"""
Super():
To invoke parent class methods
To invoke parent class variables
To invoke parent class constructor
"""
"""
Ex1:Invoking Parent class methods
"""
class A:
    def m1(self):
        print("this is method from class A")

class B(A):
    def m2(self):
        print("this is method from class B")
        super().m1()#here we are invoking parent class method using Super() keyword

b=B()
b.m2()
"""
Ex2:Invoking parent class variables
"""
# class C:
#     a,b=10,20
#
# class D(C):
#     i,j=100,200
#     def m3(self,x,y):
#         print(x+y)#local variable
#         print(self.i+self.j)#class variables of child class
#         print(self.a+self.b)#class variables of parent class
# d=D()
# d.m3(1,2)
"""
Ex:If variables has a same name then how to execute by using Super() keyword
"""
e,f=15,30
class C:
    e,f=10,20

class D(C):
    e,f=100,200
    def m3(self,e,f):
        print(e+f)
        print(self.e+self.f)
        print(super().e+super().f)#this statement will invoke the parent class variables
        print(globals()['e']+globals()['f'])

d=D()
d.m3(1,2)

"""
Ex3:How to invoke parent class constructor
"""
# class E:
#     def __init__(self):
#          print("constructor from A")
#
# class F(E):
#     pass
# objf=F()

class E:
    def __init__(self):
         print("constructor from A")

class F(E):
    def __init__(self):
        print("constructor from B")
       # super().__init__()#this ststement will invoke the parent class constructor
        E.__init__(self)#Approch2 of invoking the constructor
objf=F()


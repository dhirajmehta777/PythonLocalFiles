"""
Classes can inherit functionality of other classes
if object is created using a class that inherits from a super class
the object will containt the methods of both the class and the superclass
the same holds true for variables of both the superclass and the class that inherits from the super class
"""
"""
Types of Inheritance:
Single:Having only one parent and one child class
Multi level:having multiple child and parent classes
Hierarchical:having only one parent class for multiple child classes
Multiple:Having multiple parent class but only one child class
Hybrid:combination of hierarchical and multiple
"""
"""
Ex1:Single Inheritance
"""
class A:
    def m1(self):
        print("this is m1 method from class A")

class B(A):
    def m2(self):
        print("this is m2 method from class B")

aobj = A()
aobj.m1()

bobj = B()
bobj.m1()
bobj.m2()

"""
Ex2:Single Inheritance
"""
class C:
    x,y=100,200
    def m3(self):
        print(self.x+self.y)

class D(C):
    e,f=300,400
    def m4(self):
        print(self.e+self.f)
dobj=D()
dobj.m3()
dobj.m4()

"""
Ex3:Multi level inharitance:
"""
class E:
    p,q=100,200
    def m5(self):
        print(self.p+self.q)

class F(E):
    r,t=300,400
    def m6(self):
        print(self.r+self.t)

class G(F):
    u,v=30,50
    def m7(self):
        print(self.u+self.v)

objg=G()
objg.m5()
objg.m6()
objg.m7()

"""
Ex4:Heirarchical Inheritance
"""
class H:
    i,j=50,50
    def m8(self):
        print(self.i+self.j)

class I(H):
    k,l=10,20
    def m9(self):
        print(self.k+self.l)

class J(H):
    m,n=50,90
    def m10(self):
        print(self.m+self.n)

obji=I()
obji.m8()
obji.m9()

objij=J()
objij.m10()
objij.m8()

"""
Ex5:Multiple Inheritance:
"""
class K:
    o,p=50,50
    def m11(self):
        print(self.o+self.p)

class L:
    o1,p1=10,20
    def m12(self):
        print(self.o1+self.p1)

class M(K,L):
    o2,p2=50,90
    def m13(self):
        print(self.o2+self.p2)

objm=M()
objm.m11()
objm.m12()
objm.m13()
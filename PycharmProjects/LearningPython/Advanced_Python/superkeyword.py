class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print('Name:',self.name)
        print('Age:',self.age)

class Student(Person):
    def __init__(self,name,age,rollno,marks):
        super().__init__(name,age)
        self.rollno=rollno
        self.marks=marks
    def display(self):
        # print('Name:',self.name)
        # print('Age:',self.age)
        super().display()
        print('Roll Number:',self.rollno)
        print('Marks:',self.marks)
class Teacher(Person):
    def __init__(self, name,age,salary,subject):
        super().__init__(name,age)
        self.salary=salary
        self.subject=subject

    def display(self):
        # print('Name:',self.name)
        # print('Age:',self.age)
        super().display()
        print('Salary:',self.salary)
        print('Subject:',self.subject)
s=Student('Ravi',23,101,99)
t=Teacher('durga',62,100000,'python')
t.display()
s.display()
#here the biggest adventage of super method is to call parent class constructor and parent class method hence
#helps in code reuseability

"""
How to call a particular parent class method by using super()
We have two ways 
"""
"""
first method:Example
ParentClassName.methodName(self)
"""
class A:
    def m1(self):
        print('A class method')
class B(A):
    def m1(self):
        print('B class method')
class C(B):
    def m1(self):
        print('C class method')
class D(C):
    def m1(self):
        print('D class method')
class E(D):
    def m1(self):
        #C.m1(self)
        super(D,self).m1()#here c class m1 method will be invoked
e=E()
e.m1()

"""
using super key how to call variables
"""
class P:
    a=10
    def __init__(self):
        self.b=20

class Q(P):
    def m2(self):
        print(super().a)#from child class by using super() key we can call parent class static variable
        #print(super().b)#from child class by using super() we cannot call parent class instance variables
        #we should use self only
        print(self.b)
q=Q()
q.m2()

"""
Example:
"""
class F:
    def __init__(self):
        print('Parent Constructor')
    def m3(self):
        print('Parent Instance Method')
    @classmethod
    def m4(cls):
        print('Parent Class Method')
    @staticmethod
    def m5():
        print('Parent Static Method')

class G(F):
    # def __init__(self):
    #     super().__init__()
    #     super().m3()
    #     super().m4()
    #     super().m5()
    # def method1(self):
    #     super().__init__()
    #     super().m3()
    #     super().m4()
    #     super().m5()
    # @classmethod
    # @staticmethod weather it will work or not for any of these two decorators 
    def method1(self):
        super().__init__()
        super().m3()
        super().m4()
        super().m5()


g=G()
g.method1()

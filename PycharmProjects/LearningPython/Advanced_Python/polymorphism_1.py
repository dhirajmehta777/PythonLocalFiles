"""
polymorphism
duck typing phylosopy of python
overloading
        operator overloading
        method overloading---not supported by python
        constructor overloading---not supported by python
Overriding
        method overriding
        constructor overriding
"""
"""
What is polymorphism?
poly--->means--->many
morphs--->means--->forms
one name but multiple forms.
"""
"""
Method Overloading:
Same method name but different arrgument type.
example:
deposit(cash)
deposit(cheque)
deposit(dd)

abs(int i)
abs(float i)
abs(long i)
"""
"""
Operator Overloading:In java we are not having operator overloading concept
same operator but purposes are different.
example:
10+20=30
durga+soft=durgasoft

10*2=20
durga*2=durgadurga

operator overloading concept internally it is implemented by using magic methods
magic methods are:
+===>__add__()
-===>__sub__()
*===>__mul__()
/===>__div__()
%===>__mod__()
//===>__floordiv__()
**===>__pow__()

+= ==>__iadd__()
-= ==>__isub__()
*= ==>__imul__()
/= ==>__idiv__()
%= ==>__imod__()
//= ==>__ifloordiv__()
**= ==>__ipow__()

> ===>__gt__()
>= ===>__ge__()
< ===>__lt__()
<= ===>__le__()
== ===>__eq__()
!= ===>__ne__()

Example:
class Book:
    def __init__(self,pages):
        self.pages=pages
    
    def __add__(self,others):
        return self.pages+others.pages
    
    def __sub__(self,others):
        return self.pages-others.pages
    
    def __mul__(self,others):
        return self.pages*others.pages
b1=Book(100)
b2=Book(200)
b3=Book(300)
print(b1+b2)
print(b2+b3)
print(b1+b2+b3)--->throws error
print(b1+b2)
print(b1-b2)
print(b1*b2)
"""
"""
Example2:__str__()

class Book:
def __init__(self,pages):
    self.pages=pages

def __str__(self):
    return 'The number of pages:'str(self.pages)

b1=Book(100)
print(b1)
o/p===>The number of pages:100
"""
"""
Example3:
class Book:
def __init__(self,pages):
    self.pages=pages

def __str__(self):
    return 'The number of pages:'str(self.pages)

def __add__(self,others):
    total=self.pages+others.pages
    b=Book(total)
    return b

b1=Book(100)
b2=Book(200)
b3=Book(300)
b4=Book(700)
print(b1+b2+b3+b4)
"""
"""
Whenever we are calling + operator then __add__() method will be called.
Whenever we are printing Book object reference then __str__ method will be called.
If we are not providing this method then befault implementation will be executed.
"""
"""
Example3:
"""
# class Student:
#     def __init__(self, name,marks):
#         self.name=name
#         self.marks=marks
#
#     def __lt__(self,other):
#         return self.marks<other.marks
# s1=Student('durga',100)
# s2=Student('ravi',200)
# print(s1<s2)
# print(s2<s1)

"""
Example3:
"""
# class Employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#
#     def __mul__(self, other):
#         return self.salary*other.days

# class TimeSheet:
#     def __init__(self,name,days):
#         self.name=name
#         self.days=days
#
#     def __mul__(self,other):
#         return self.days * other.salary
#
# e=Employee('Durga',500)
# t=TimeSheet('Durga',25)
# print('This Month Salary:',e*t)
# print('This Month Salary:',t*e)#

"""
In python, within a class if we have two methods have same name but different argument then there method overloading
concept came into the picture but here while calling the method it will consider only the last method 
irrespective of arguments
"""
"""
Example1:
"""
# class Test:
#     def m1(self):
#         print('No arg method')
#
#     def m1(self,x):
#         print('one arg method')
# t=Test()
# t.m1(10)

"""
Python wont provide support to method/constructor overloading because we wont declare any type for the variable
"""
"""
python supports default argument and variable length argument
"""
"""
Example for default argument
"""
# class Test:
#     def sum(self,a=None,b=None,c=None):
#         if a!=None and b!=None and c!=None:
#             print('the sum of 3 numbers:',a+b+c)
#         elif a!=None and b!=None:
#             print('the sum of 2 numbers:',a+b)
#         else:
#             print('please provide 2 or 3 arguments')
# t=Test()
# t.sum(10,20,30)
# t.sum(10,20)
# t.sum(10)

"""
Example for variable length argument
"""
# class Test:
#     def sum(self,*a):
#         total=0
#         for x in a:
#             total=total + x
#         print('The sum:',total)
# t=Test()
# t.sum(10,20)
# t.sum(10,20,30)
# t.sum(10,20,30,40)
# t.sum()
# t.sum(10)

"""
Example
# """
# class Test:
#     def m1(self,*a):
#         total=''
#         for x in a:
#             total=total + x
#         print('The Result:',total)
# t=Test()
# t.m1('durga')
# t.m1('durga','software')
# t.m1('durga','software','solutions')

"""
Inheritance Example
"""
class P:
    def property(self):
        print('cash+land+gold+power')

    def marry(self):
        print('sita')

class C(P):
    def marry(self):
        super().marry()
        print('kat...')
c=C()
c.property()
c.marry()

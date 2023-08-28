class ParentClass:

    def __init__(self):
        print("parent class instance")

    def parent_method(self):
        print("parents money")

class ChildClass(ParentClass):
    pass

c1=ChildClass()
c1.parent_method()
# p1=ParentClass()
# p1.parent_method()
#################################################################
class RateOfInterest:
    interest=0.06
    def __init__(self,name,loan):
        self.name=name#instance variable
        self.loan=loan#instance variable

    def calc_interest(self):
        print("Total Interest: ", self.loan * RateOfInterest.interest)

class Student(RateOfInterest):
    interest = 0.04
s=Student('mantan',5000000)
s.calc_interest()
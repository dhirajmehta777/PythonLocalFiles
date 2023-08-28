class Employee:
    #pass#if you dont want to put any details inside class then we can just write pass
    def __init__(self,fname,lname,email):
        self.fname=fname
        self.lname=lname
        self.email=email

    def greet_person(self):
        print("hellow, welcome "+self.fname,self.lname,self.email)

emp1=Employee('Maneet', 'Mehra','mm2546@gmail.com')
emp2=Employee('ram','singh','rs434@gmail.com')
#using object reference variable we can access the employee details
print(emp1.fname)
print(emp2.lname)
#using object refernce variable we can call the method i.e greetperson
emp1.greet_person()
emp2.greet_person()
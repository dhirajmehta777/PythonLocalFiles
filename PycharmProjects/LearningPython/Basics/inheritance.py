class A():
    
    def display(self):
        print("This is class A")

class B(A):
     def display2(self):
         print("This is class B")

obj=B()
obj.display()
obj.display2()
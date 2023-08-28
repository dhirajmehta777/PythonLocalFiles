#in order to create a class simply we have to use class keyword follwed by class name
#here within these class we need to initiate the variables so we need to use the
#init method same as that of constructor, whenever you are creating an object of this class
#that init method will be called.
        #this init method takes the arrgument self, this self keyword used as refernce to the object
        #when you instantiate this particular class then this self will refernce to the object
        # that are been created by using this particular class
        #this init method basically act as a constructor basically to construct an object

#if we want to create our own method here it is

#here self is a parameter by default needs to be passed while creating the method
        #whenever im calling or creating an object of these particular class and calling
# these particular method then i will return the area
class AreaRect:

    def __init__(self,l,b): #init method
        self.l=l
        self.b=b

    def calculate_area(self): #our own method i.e.custom method
        return self.l*self.b

area1=AreaRect(8,5) #object created for these class, area1 is a reference variable that holds these object
print(area1.calculate_area())
are2=AreaRect(10,5)
print(are2.calculate_area())







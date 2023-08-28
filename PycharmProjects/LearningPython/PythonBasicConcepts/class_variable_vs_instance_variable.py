class RateOfInterest:
    interest=0.06#this is class level varieable and it is defined below class nd outside the method.
    #And this varieable is accessable to all the objects that will created using this class
    # def __init__(self,name,loan,interest):
    #     self.name=name#instance variable
    #     self.loan=loan#instance variable
    #     self.interest=interest#instance variable

    # def calc_interest(self):
    #      print("Total Interest: ",self.loan*self.interest)
    #
    # p1=RateOfInterest("Ram",5000000,0.06)
    # p1.calc_interest()
    #
    # p2=RateOfInterest("john",4000000,0.06)
    # p2.calc_interest()

    def __init__(self,name,loan):
        self.name=name#instance variable
        self.loan=loan#instance variable
        # self.interest=interest#Now this is defined at class level and here its not required

    def calc_interest(self):
         # print("Total Interest: ", self.loan * self.interest)#here self refers to the particular
         # instance, so to refraze the class variable is not tied to aparticular object it is
         # accessible to all and instance variable is a variable basically that is tied to particular
         # object that you create within that particular class

         print("Total Interest: ", self.loan * RateOfInterest.interest)

p1 = RateOfInterest("Ram", 5000000)
#p1.interest=0.08 #this is possible bcz of self keyword if we use RateOfInterest.interest its not possible
RateOfInterest.interest=0.08 #we can change the class level variable by using class name.interest
p1.calc_interest()

p2 = RateOfInterest("john", 4000000)
#p2.interest=0.04
RateOfInterest.interest=0.04
p2.calc_interest()


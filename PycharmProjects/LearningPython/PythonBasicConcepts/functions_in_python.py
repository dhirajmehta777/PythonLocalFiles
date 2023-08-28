#python function or any function when we say in programming language basicall
#it is set of steps that you define within a piece of code that you can reuse at
#multiple places, just we need to define the function and reuse it where ever its required
"""
say for example there is a login page, so login functionality or login process can be captured within the
one function and then when ever you are trying to write a particular testcase which require login
you just call that login function and provide the username and password
"""

# def addition():
#     print(12+10)
###############################################
# x=10
# y=22
# def addition():
#     print(x+y)
###################################################
a = 10
b = 20

def addition(x,y):#x,y are parameters
    print(x+y)
addition(a,b)#we can call this function multiple times hence we can reuse it
addition(10,20)#10,12,10,20 are arguments
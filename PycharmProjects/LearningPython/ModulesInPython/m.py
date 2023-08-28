# class A:
#     pass
# class B:
#     def m1(self):
#         print("this is m1 method")
#
#     def m2(self):
#         print("this is m2 method")
#########################################################
#if the same methods are wrriten outside classes then they are called as functions not methods
# and if we run dir() command in the main.py then now it will dispaly how many number of functions are
# created inside the python file or m module but if the same functions are placed inside the class
# then they are called as methods and these methods cant be counted by dir() command
def m1(self):
        print("this is m1 method")

def m2(self):
        print("this is m2 method")
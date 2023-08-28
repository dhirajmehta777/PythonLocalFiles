"""
Exception is an abnormal condition.
Exception is an event that disrupts the normal flow of the program
Errors will occur due to programing mistake.
Exception occurs due to invalid user input.
"""
"""
Exception handling keyword:
try
except
else
finally
"""
"""
Ex1:Without handling exception 
"""
# print("program is started")
# print(10/0)
# print("program is completed")

"""
Ex2:With handling exception. the program will not terminate abnormally.
"""
# print("program is started")
# try:
#     print(10/0)#user invalid inout
# except ZeroDivisionError:
#     print("Entered into except block-Handled Exception")
# print("program is completed")
"""
Ex3:using valid user input
"""
# print("program is started")
# try:
#     print(10/5)#here it will not enter into except block, since its a valid user input
# except ZeroDivisionError:
#     print("Entered into except block-Handled Exception")
# print("program is completed")
"""
Ex4:for one try block you can have a multiple except block
"""
# print("program is started")
# try:
#     print(10/0)
# except TypeError:#this will through an error
#     print("Entered into except block-Handled TypeError")
# except ZeroDivisionError:#this will handle the exception
#     print("Entered into except block-Handled ZeroDivisionError")
# print("program is completed")
"""
Ex5:else block along with try except block, if none of the except block will handle the exception then 
else block will execute, provided the user input must be valid one.
#case1:thrown exception--->except block will execute
case2:not thrown any exception then else block will execute
"""
# print("program is started")
# try:
#     print(10/5)
# except TypeError:#this will through an error
#     print("Entered into except block-Handled TypeError")
# except SyntaxError:#this will handle the exception
#     print("Entered into except block-Handled ZeroDivisionError")
# else:
#     print("entered into else block")
# print("program is completed")
"""
Ex6:finally block will execute always weather there may be or may not be any exception
case1:Exception occurs-->except block will execute along with finally block
case2:Exception occured-->not handled-->still finally block will execute
case3:Exception not occured-->except block will not execute-->else and finally will execute
Statements under else block run only when no exception is rised.
Statements in finally block will run every time no matter exception occur or not
"""
print("program is started")
try:
    print(10/5)
except TypeError:#this will through an error
    print("Entered into except block-Handled TypeError")
except SyntaxError:#this will handle the exception
    print("Entered into except block-Handled ZeroDivisionError")
else:
    print("entered into else block")
finally:
    print("entered into finally block")
print("program is completed")
"""
Ex7:Raising Exceptions,To raise your exception from your own methods you need to use raise keyword
syntax:raise ExceptionClass("your arrgument") 
"""
def enterage(age):
    if age < 0:
        raise  ValueError("only positive integers are allowed")#we have raised our own exception
    if age%2==0:
        print("age is even")
    else:
        print("age is odd")
try:
    num=-5
    enterage(num)
except ValueError:
    print("only positive integers are allowed")
except:
    print("something is wrong")

"""
Ex8:Use Exception Objects
"""
try:
    number=one
    print("the number is:", number)
except NameError as ex:
    print("An Exception is:", ex)

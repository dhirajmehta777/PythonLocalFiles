"""
Lambda Function:
A function which has no name, is known as lambda function
this is also known as anonymous function
A lambda function can take any number of arguments, but can only have one expression.
Syntex:lambda arguments:expression
"""
x=lambda a: a+10
print(x(5))

y=lambda b,c:b+c
print(y(5,5))

z=lambda e,f,g:e+f+g
print(z(1,2,3))

#but same thing if we wont use lambda function then
def add(a):
    a=a+10
    return a
print(add(10))
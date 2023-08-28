#while loop
#used to iterate block of code as long as test expression is true
#test expression is checked first, if expression is evaluated to true then body of loop executed
#conditions are used to stop the loops
#can iterate on lists, strings, tuples and dictionary
#syntax of while loop
#while test_expression
#    body of while loop

x=0
while x<=10:
    print(x)
    x=x+1 #this condition is used to stop the loop else the loop will run infinately
    print("inside while loop")
print("out of the while loop")

city="pune"
y=0
while y<len(city):
    print(city[y])
    y=y+1

#explore how to iterate while loops on lists tuple and dictionary


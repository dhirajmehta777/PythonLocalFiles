#break:breaks out from the nearest enclosing loop
#continue:go to the start of the nearest enclosing loop
#
#while <expression>:
    #<statement(s)>
    #break
    #<statement(s)>
    #continue
    #<statement(s)>
#<statement(s)>
#
#else clause:
#while <expression>:
    #<statement(s)>
#else
    #<statement(s)>


# x=0
# while x<=10:
#     print(x)
#     x=x+1 #this condition is used to stop the loop else the loop will run infinately
#     #break#this will brake the loop here and will not proceed further o/p=0(zero) prints only one value
#     continue #this will contiue to print 0 to 10 with out going into print statement next to it.
#     #if we do not use continue then inside value loop will print after each digit
#     print("inside while loop")
# print("out of the while loop")

x=0
y=0
while x<=10:
    print(x)
    x=x+1
    print("parent loop")
    while y<5:
        print(y)
        y=y+1
        continue
        print("inner while loop")
print("out of loop")

q=0
while q<=10:
    print(q)
    q=q+1
    if q==5:
        break #here else block will not execute
else:
    print("out of the while else loop") #if else block is not used then this print statement
    # prints eventhough we applied break.
    